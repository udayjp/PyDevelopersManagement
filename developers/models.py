from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Weightage(models.Model):
    projects=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],blank=True,null=True)
    blogs=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],blank=True,null=True)
    qas=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],blank=True,null=True)
    class Meta:
        verbose_name = "Weightage"
        verbose_name_plural = "Weightages"
            

class Technology(models.Model):
    name=models.CharField(max_length=255)
    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"
    def __str__(self):
        return self.name

class Domain(models.Model):
    name=models.CharField(max_length=255)
    class Meta:
        verbose_name = "Domain"
        verbose_name_plural = "Domains"
    def __str__(self):
        return self.name

class Project(models.Model):
    name=models.CharField(max_length=255)
    rating=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=255)
    rating=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
    def __str__(self):
        return self.title

class QA(models.Model):
    question=models.CharField(max_length=255)
    rating=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    class Meta:
        verbose_name = "QA"
        verbose_name_plural = "QAs"
    def __str__(self):
        return self.question

class Developer(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    technology=models.ManyToManyField(Technology)
    domain=models.ManyToManyField(Domain)
    projects=models.ManyToManyField(Project)
    blogs=models.ManyToManyField(Blog)
    qa=models.ManyToManyField(QA)    
    score=models.FloatField(blank=True,null=True)


    class Meta:
        verbose_name = "Developer"
        verbose_name_plural = "Developers"

    def __str__(self):
        return self.name

    def getScore(self):        
        score = 0    
        projectRating =0
        blogRating =0
        qaRating =0

        for project in self.projects.all():
            projectRating +=project.rating
        for blog in self.blogs.all():
            blogRating += blog.rating
        for q in self.qa.all():
            qaRating += q.rating
        
        weightages=Weightage.objects.get(pk=1)
    
        projWeightage=weightages.projects
        blogWeightage=weightages.blogs
        qaWeightage=weightages.qas

        projectScore=(projWeightage*projectRating)/(5*len(self.projects.all()))
        blogScore=(blogWeightage*blogRating)/(5*len(self.blogs.all()))
        qaScore=(qaWeightage*qaRating)/(5*len(self.qa.all()))  

        score=projectScore+blogScore+qaScore
        
        score=(score*100)/(projWeightage+blogWeightage+qaWeightage)

        self.score =  "{:.2f}".format(score)
        self.save()  
        return self.score      

