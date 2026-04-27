from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

from Article.models import *
from Contact.models import *
from Personal_Information.models import *
from Project.models import *
from Website_settings.models import *
from Profile_url.models import *

def contactform(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        en=Contact(name=name,email=email,subject=subject,message=message)
        en.save()
    return render(request,"success.html")

def Data(request):
    # ================ [ Personal Information ] ================
    Profile_data = Profile.objects.all()
    Education_data = Education.objects.all()
    Certification_data = Certification.objects.all()
    Experience_data = Experience.objects.all()
    Skill_data = Skill.objects.all()

    # ================ [ website settings ] ================
    WebSettings_data = WebSettings.objects.first()
    SEOSettings_data = SEOSettings.objects.all()

    # ================ [ Project ] ================
    PortfolioCategory_data = PortfolioCategory.objects.all()
    Portfolio_data = Portfolio.objects.all()
    Work_data = Work.objects.all()

    # ================ [ Article ] ================
    Category_data = Category.objects.all()
    Tag_data = Tag.objects.all()    
    Article_data = Article.objects.all().order_by('-id')
    Profile_url_data = Profile_url.objects.all()[:1]
    data = {
        'Profile_data':Profile_data,
        'Education_data':Education_data,
        'Certification_data':Certification_data,
        'Experience_data':Experience_data,
        'Skill_data':Skill_data,

        'WebSettings_data':WebSettings_data,
        'SEOSettings_data':SEOSettings_data,

        'PortfolioCategory_data':PortfolioCategory_data,
        'Portfolio_data':Portfolio_data,
        'Work_data':Work_data,

        'Category_data':Category_data,
        'Tag_data':Tag_data,
        'Article_data':Article_data,

        'Profile_url_data':Profile_url_data,
    }
    return render(request,"index.html",data)
def robots_txt(request):
    robot_text = SEOSettings_data.robots()
    return HttpResponse(
        "User-agent: *\n"
        "Disallow:\n\n"
        "Sitemap: https://anonymous2583.pythonanywhere.com/sitemap.xml",
        content_type="text/plain"
    )
def article(request,type_id):
    Profile_data = Profile.objects.all()[:1]
    Article_data = get_object_or_404(Article, pk=type_id)
    WebSettings_data = WebSettings.objects.first()
    Article_data.views += 1
    Article_data.save()
    data = {
        'Profile_data':Profile_data,
        'WebSettings_data':WebSettings_data,
        'Article_data':Article_data,
    }
    return render(request,"blog.html",data)

def like_post(request, type_id):
    Article_data = get_object_or_404(Article, pk=type_id)
    Article_data.likes += 1
    Article_data.save()
    return redirect(f'/articles/{type_id}/')
