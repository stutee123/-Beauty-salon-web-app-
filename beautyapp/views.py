from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .filters import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'beautyapp/home.html')

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user=form.save()
            login(request, user)
            return render(request, 'beautyapp/home.html')
    return render(request, 'beautyapp/register.html', {"form":form})


def services(request):
    services=Services.objects.all()
    myFilter = ServicesFilter(request.GET, queryset=services)
    services=myFilter.qs
    return render(request, 'beautyapp/services.html',{"services":services,"myFilter":myFilter})

def blogs(request):
    blogs= Blog.objects.all()
    myFilter = BlogFilter(request.GET, queryset=blogs)
    blogs=myFilter.qs
    
    return render(request, 'beautyapp/blog.html',{"myFilter":myFilter,"blogs":blogs})

def fullBlogs(request, blog_id):
    blog= get_object_or_404(Blog, id=blog_id)
    return render(request, 'beautyapp/fullblogs.html',{"blog":blog})


def blogDetail(request, blog_id):
    
    template_name = 'beautyapp/fullblogs.html'
    post=get_object_or_404(Blog, id=blog_id)
    comments = post.comments.filter(active=True)
    new_comments = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comments = comment_form.save(commit=False)
            new_comments.post = post
            new_comments.save()
    else:
        comment_form = CommentForm()
    return render(request, template_name, {'post':post, 'comments':comments,'new_comments':new_comments,'comment_form':comment_form})

def haircare(request):

    haircares=HairCare.objects.all()
    myFilter = HairCareFilter(request.GET, queryset=haircares)
    haircares=myFilter.qs
    
    if request.method == 'POST':
        filled_form = BookingHairCareForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = "Thank you for booking an appointment.    Your appointment for %s is booked for %s." %(filled_form.cleaned_data['haircare'],
            filled_form.cleaned_data['date'],)
            new_form = BookingHairCareForm()
            return render(request, 'beautyapp/haircare.html',{'haircares':haircares,"myFilter":myFilter,'bookinghaircareform':new_form,'note':note})
    else:
        form = BookingHairCareForm()
        return render(request, 'beautyapp/haircare.html',{'haircares':haircares,"myFilter":myFilter,'bookinghaircareform':form})

    
def makeupservice(request):

    makeupservices=MakeUpServices.objects.all()
    myFilter = MakeUpServicesFilter(request.GET, queryset=makeupservices)
    makeupservices=myFilter.qs
    
    if request.method == 'POST':
        filled_form = BookingMakeUpServicesForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = "Thank you for booking an appointment.    Your appointment for %s is booked for %s." %(filled_form.cleaned_data['makeupservices'],
            filled_form.cleaned_data['date'],)
            new_form = BookingMakeUpServicesForm()
            return render(request, 'beautyapp/makeupservice.html',{"makeupservices":makeupservices,'myFilter':myFilter, 'bookingmakeupserviceform':new_form,'note':note})
    else:
        form = BookingMakeUpServicesForm()
        return render(request, 'beautyapp/makeupservice.html',{"makeupservices":makeupservices,'myFilter':myFilter, 'bookingmakeupserviceform':form})       

def facialtreatment(request):

    facialtreatments=FacialTreatment.objects.all()
    myFilter = FacialTreatmentFilter(request.GET, queryset=facialtreatments)
    facialtreatments=myFilter.qs

    if request.method == 'POST':
        filled_form = BookingFacialTreatmentForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = "Thank you for booking an appointment.    Your appointment for %s is booked for %s." %(filled_form.cleaned_data['facialtreatment'],
            filled_form.cleaned_data['date'],)
            new_form =BookingFacialTreatmentForm()
            return render(request, 'beautyapp/facialtreatment.html',{'facialtreatments':facialtreatments,'myFilter':myFilter, 'bookingfacialtreatmentform':new_form,'note':note})
    else:
        form = BookingFacialTreatmentForm()
        return render(request, 'beautyapp/facialtreatment.html',{ 'facialtreatments':facialtreatments,'myFilter':myFilter,'bookingfacialtreatmentform':form})    

def nailart(request):

    nailarts=NailArts.objects.all()
    myFilter = NailArtFilter(request.GET, queryset=nailarts)
    nailarts=myFilter.qs

    if request.method == 'POST':
        filled_form = BookingNailArtsForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = "Thank you for booking an appointment.    Your appointment for %s is booked for %s." %(filled_form.cleaned_data['nailarts'],
            filled_form.cleaned_data['date'],)
            new_form =BookingNailArtsForm()
            return render(request, 'beautyapp/nailart.html',{ "nailarts":nailarts,'myFilter':myFilter,'bookingnailartform':new_form,'note':note})
    else:
        form = BookingNailArtsForm()
        return render(request, 'beautyapp/nailart.html',{"nailarts":nailarts, 'myFilter':myFilter,'bookingnailartform':form})    

def hairstyle(request):

    hairstyles=HairStyles.objects.all()
    myFilter = HairStyleFilter(request.GET, queryset=hairstyles)
    hairstyles=myFilter.qs

    if request.method == 'POST':
        filled_form = BookingHairStylesForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = "Thank you for booking an appointment.    Your appointment for %s is booked for %s." %(filled_form.cleaned_data['hairstyles'],
            filled_form.cleaned_data['date'],)
            new_form =BookingHairStylesForm()
            return render(request, 'beautyapp/hairstyle.html',{"hairstyles": hairstyles,'myFilter':myFilter,'bookinghairstyleform':new_form,'note':note})
    else:
        form = BookingHairStylesForm()
        return render(request, 'beautyapp/hairstyle.html',{"hairstyles": hairstyles, 'myFilter':myFilter,'bookinghairstyleform':form})    


def pedicure(request):

    pedicures=Pedicure.objects.all()
    myFilter = PedicureFilter(request.GET, queryset=pedicures)
    pedicures=myFilter.qs

    if request.method == 'POST':
        filled_form = BookingPedicureForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = "Thank you for booking an appointment.    Your appointment for %s is booked for %s." %(filled_form.cleaned_data['pedicure'],
            filled_form.cleaned_data['date'],)
            new_form =BookingPedicureForm()
            return render(request, 'beautyapp/pedicure.html',{"pedicures":pedicures,'myFilter':myFilter,'bookingpedicureform':new_form,'note':note})
    else:
        form = BookingPedicureForm()
        return render(request, 'beautyapp/pedicure.html',{ "pedicures":pedicures,'myFilter':myFilter,'bookingpedicureform':form})  


def manicure(request):

    manicures=Manicure.objects.all()
    myFilter = ManicureFilter(request.GET, queryset=manicures)
    manicures=myFilter.qs

    if request.method == 'POST':
        filled_form = BookingManicureForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = "Thank you for booking an appointment.    Your appointment for %s is booked for %s." %(filled_form.cleaned_data['manicure'],
            filled_form.cleaned_data['date'],)
            new_form =BookingManicureForm()
            return render(request, 'beautyapp/manicure.html',{"manicures":manicures,'myFilter':myFilter,'bookingmanicureform':new_form,'note':note})
    else:
        form = BookingManicureForm()
        return render(request, 'beautyapp/manicure.html',{"manicures":manicures,'myFilter':myFilter,'bookingmanicureform':form})  

def fullServices(request):
    return render(request, 'beautyapp/fullservices.html')