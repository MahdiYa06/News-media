from django.db import models
from utils.base import TimeStampModel



class Category(TimeStampModel):
    title = models.CharField("Title", max_length=50)
    description = models.TextField("Description")
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'Categories'
    
    
class Article(TimeStampModel):
    category = models.ForeignKey("article.Category", verbose_name="Category", on_delete=models.PROTECT, related_name='articles')
    title = models.CharField("Title", max_length=250)
    content = models.TextField("Content")
    
    
    
    def __str__(self) -> str:
        return f'{self.title}({self.category.title})'
    
    class Meta:
        db_table = 'Articles'
    
    
    
class DailyCategorySummary(TimeStampModel):
    category = models.OneToOneField("article.Category", verbose_name="Category", on_delete=models.PROTECT, related_name='summary_text')
    title = models.CharField("Title", max_length=250)
    content = models.TextField("Content")
    
    
    def __str__(self) -> str:
        return f'{self.title}({self.category.title})'
    
    class Meta:
        db_table = 'DailyCategorySummaries'
    
        
    
class Report(TimeStampModel):
    summary = models.OneToOneField("article.DailyCategorySummary", verbose_name="Summary", on_delete=models.CASCADE, related_name='report')
    status = models.BooleanField("Status")
    
    
    
    def __str__(self) -> str:
        return self.summary_id.title
    
    class Meta:
        db_table = 'Reports'
    
   
class ReportLine(TimeStampModel):
    report = models.OneToOneField("article.Report", verbose_name="Report", on_delete=models.CASCADE, related_name='lines')
    user = models.ForeignKey("user.User", verbose_name="User", on_delete=models.CASCADE, related_name='users')
    status = models.BooleanField("Status")   
    
    
    
    def __str__(self) -> str:
        return self.report.summary_id.category
    
    class Meta:
        db_table = 'ReportLines'
        
        
        
class Notification(TimeStampModel):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE, related_name='notifs') 
    category = models.ManyToManyField("article.Category", verbose_name="Category", on_delete=models.PROTECT)