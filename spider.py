#-*- coding: utf-8 -*-
import requests
import random
import json
import time
from labelFilter import html_filter
from outToTxt import outTxt
from outToDb import Connetction
from analyzeHtml import searchContentById

def searchQuestionByTopic(topicId, sum=100, pageSize=10, pageNum=1):
    questionSet=set()
    #  ua_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
    #  虚拟header头部
    headers = [{
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'},
        {
        }]
    header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    #  example topicI=19550447
    # #  分页查询页码
    # pageNum=0
    # #  分页查询页大小
    # pageSize=10
    cnt = 0
    while (True):
        url1 = "https://www.zhihu.com/api/v4/topics/" + str(topicId) + "/feeds/essence?include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.annotation_detail%2Ccomment_count%3B&limit=" + str(pageSize) + "&offset=" + str(pageSize * pageNum)
        pageNum = pageNum + 1
        # 随机header编码，据说防封
        head_No = random.randint(0, len(headers) - 1)
        req = requests.get(url1, headers=header)
        req_str=req.text
        req_json=json.loads(req_str)

        if req_json['paging']['is_end']:
            break
        data = req_json['data']
        for item in data:
            if ("question" in item["target"]):  # 结果里可能包含文章，不是question,排除
                qid = item["target"]["question"]["id"]
                if(not qid in questionSet):
                    questionSet.add(qid)
                    # 热门提问
                    cnt = cnt + 1
                    print(cnt)
                    question_title = item["target"]["question"]["title"]
                    question_content=searchContentById(qid)
                    # print(question_title+question_content)
                    c=Connetction()
                    new_qid=c.insertQuestion(question_title=question_title,question_content=question_content,user_id=random.randint(1,20))
                    # top_answer=item["target"]["content"]
                    # 搜索问题下面的回答
                    searchAnswersByQid(qid,question_db_id=new_qid,sum=50)
                    if (cnt >= sum):
                        return
def searchAnswersByQid(qid,question_db_id,limit=10, pageNum=0,sum=50):
    print(qid)
    cnt = 0
    while(True):
        url = "https://www.zhihu.com/api/v4/questions/" + str(
            qid) + "/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=" + str(
            limit) + "&offset=" + str(pageNum * limit) + "&platform=desktop&sort_by=default"
        headers = [
            {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'},
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'},
            {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'},
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'},
        ]
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
        #head_No = random.randint(0, len(headers) - 1)
        req = requests.get(url, headers=header)
        req_str = req.text
        res_json = json.loads(req_str)
        data = res_json["data"]
        pageNum=pageNum+1
        for item in data:
            cnt = cnt + 1
            if cnt>sum:
                return
            author = item["author"]["name"]
            answer_content = item["content"]
            question_title = item["question"]["title"]
            print("downloading "+ str(cnt)+ "/" + str(res_json["paging"]["totals"])+"\r")
            # outTxt(("downloading "+ str(cnt)+ "/" + str(res_json["paging"]["totals"])+"\r").encode('utf-8'))
            print(question_title)
            #outTxt(question_title)
            print(html_filter(answer_content))
            #outTxt(html_filter(answer_content))
            c = Connetction()
            c.insertComment(comment=html_filter(answer_content),entityId=question_db_id,userId=random.randint(1,20) )

        if res_json["paging"]["is_end"] == True or cnt >= res_json["paging"]["totals"]:
            break
if __name__ == '__main__':
    start=time.time()
    searchQuestionByTopic(19550517,sum=100)
    #searchAnswersByQid(41047159,sum=10)
    end=time.time()
    print("本次任务花费了"+str(end-start)+"s")
    # target = 'http://baidu.com/'
    # req = requests.get(url=target)
    # print(req.text)

