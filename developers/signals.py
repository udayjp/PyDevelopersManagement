from django.db.models.signals import pre_save, post_save,m2m_changed
from django.dispatch import receiver
from .models import Developer,Weightage

@receiver(post_save, sender=Developer)
def pre_save_developer(sender, instance, **kwargs):
    score = 0    
    projectRating =0
    blogRating =0
    qaRating =0
    for project in instance.projects.all():
        projectRating +=project.rating
    for blog in instance.blogs.all():
        blogRating += blog.rating
    for q in instance.qa.all():
        qaRating += q.rating
    print("instance",instance)

    weightages=Weightage.objects.get(pk=1)
   
    projWeightage=weightages.projects
    blogWeightage=weightages.blogs
    qaWeightage=weightages.qas

    projectScore=(projWeightage*projectRating)/(5*len(instance.projects.all()))
    blogScore=(blogWeightage*blogRating)/(5*len(instance.blogs.all()))
    qaScore=(qaWeightage*qaRating)/(5*len(instance.qa.all()))  

    score=projectScore+blogScore+qaScore
    
    instance.score =  "{:.2f}".format(score)