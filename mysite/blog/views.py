from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import View
from django.views.generic import CreateView, FormView

from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.template import Context, Template
from django.http import HttpResponse
from blog.models import *
from django.views.generic.list import ListView

from django.http import HttpResponseRedirect


class PostListView(ListView, FormView):
    model = Post
    template_name = "post_list.html"
    form_class = PostForm


class CommentCreateView(View):

    def post(self, request, post_pk, *args, **kwargs):
        post = Post.objects.get(pk=post_pk)
        comment_pk = request.POST.get('comment_pk')
        if comment_pk:
            comment = Comment.objects.get(pk=comment_pk)

            Comment(
                author=request.user, text_massage=request.POST['text'],
                answer_massage=post, parent=comment
            ).save()

        else:
            Comment(
                author=request.user, text_massage=request.POST['text'],
                answer_massage=post
            ).save()

        return HttpResponseRedirect('/')


def post_add(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            x = form.save(commit = False)
            x.author = request.user
            x.save()
    return redirect("/")


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail_2', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit_2.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post_blog, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail_2', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit_2.html', {'form': form})



#
def test(request):
    template = Template(open(r"D:/hlam/test.html").read())
    context = Context({"my_name": "Adrian"})
    template = template.render(context)
    
    return HttpResponse(template)
    #return render(request, 'test.html', {})








def test2(request):
    

    class R():
        

            
        def __init__(self):
            self.val=11
            
        """def __get__(self, obj, objtype):
            return self.val"""

        def __getitem__(self,index):
            return "Ну допустим индекс " + str(index)

        def __call__(self,x):
            return "Вот мы и вызвали метод"

    class Tipa_dict(dict):
        test = R()
        def __getattr__(self,name):
                return getattr(dict,name)
            
    primer = Tipa_dict()

    primer['test']=10
    print(primer)
    print(primer['test'])
    print(primer.test)
    print(primer.test(1))
    print(primer.test[0])
    

    return render(request, 'blog/variable.html', {'primer': primer})


def test_tags(request):

    variables={'x':0,'y':[]}
    variables['iter']= [(0,"Ноль"),(1,"one") ]
    variables['dic'] = dict([(0,"Ноль"),(1,"one"),("f","one_")] )

    return render(request, 'blog/tags.html', variables)




def filters(request):

    variables={'x':"привет"}
    variables["many_words"]="The effect depends on the border-color value."
    variables["smbl"]="e"
    

    return render(request, 'blog/filters.html', variables)

def urli(request,*c,**d):
    print(request.__dict__.keys())

    return render(request, 'blog/urli.html', {'c':c,'d':d})


def urli2(request,*c,**d):
    # проверки
    return redirect('urli', a='10')

















    
