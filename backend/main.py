from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class IntentRequest(BaseModel):
    text: str

class QARequest(BaseModel):
    query: str

class Feedback(BaseModel):
    user_id: str
    content: str

@app.post('/intent')
def intent_classify(req: IntentRequest):
    # 简单关键字判断示例
    text = req.text.lower()
    if any(w in text for w in ['价格','多少钱']):
        intent = 'price_inquiry'
    elif any(w in text for w in ['如何','怎样']):
        intent = 'qa'
    else:
        intent = 'general'
    return {'intent': intent}

@app.post('/qa-search')
def qa_search(req: QARequest):
    # 简易知识库模拟
    KB = {'退货': '您可以在购买后30天内申请退货。',
          '发货': '我们会在24小时内完成发货。'}
    answer = KB.get(req.query, '很抱歉，未找到相关信息。')
    return {'docs': answer}

@app.post('/feedback')
def feedback(req: Feedback):
    # 这里可写入数据库或日志文件
    with open('feedback.log', 'a', encoding='utf-8') as f:
        f.write(f"{req.user_id}:{req.content}\n")
    return {'status': 'ok'}