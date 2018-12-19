from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from django.shortcuts import render
from .models import Question,Choice

# 演化过程：
# Create your views here.
# def index(request):
#     return HttpResponse("""
#         <html>
#             <head>
#             </head>
#             <body>
#                 <h1>hello world</h1>
#             </body>
#         </html>
#     """)
# def index(request):
#     """
#     展示问题列表
#     :return:
#     """
#     question_list=Question.objects.all().order_by('-pub_date')[0:5]
#     # print(question_list)
#     # output=''
#     # for q in question_list:
#     #     print(q.id,q.question_text,q.pub_date)
#     #     output=output + q.question_text+ ','
#     # print(output)
#
#     # output=','.join([q.question_text for q in question_list])
#
#     template=loader.get_template('polls/index.html')
#     context={
#         'question_list':question_list
#     }
#
#     return HttpResponse(template.render(context,request))


def index(request):
    question_list=Question.objects.order_by('-pub_date')[:5]
    context={
        'question_list':question_list
    }
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    """
    显示一个问题的详细信息，问题内容、问题发布时间、选项内容、每个选项投票数。
    """
    try:
        question=Question.objects.get(id=question_id)

        # 写法一：（基本思想）Choice.objects.filter(question_id=question.id)
        #由于orm代劳，question直接带出对应的choices
        # 写法二：choices=Question.choice_set.all()
        #由于前端模板语言本质是后端代码，可以把上句话放html页面中写，有助于降低后端复杂度
    except Question.DoesNotExist:
        raise Http404('404,此id错误不存在')
    print(question)
    context={
        'question':question
    }
    #写法二：
    # # question=Question.objects.filter(id=question_id)
    # # if not question:
    # #     raise Http404()
    #
    # return render(request,'polls/detail.html',context)

    #  写法三：
    # question =get_object_or_404(Question, id=question_id)
    # return render(request,'polls/detail.html',{'question':question})
    return render(request,'polls/detail.html',context)
def results(request, question_id):
    """
    投票结果

    """
    pass
def vote(request,question_id):
    """
    投票

    """