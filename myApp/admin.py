from django.contrib import admin

# Register your models here.
from .models import Grades,Students

@admin.register(Grades)
class GradeAdmin(admin.ModelAdmin):
    def name(self):
        return self.gname
    name.short_description = '班级'
    def gdatetime(self):
        return self.gdate
    gdatetime.short_description = '入学时间'
    def girlnum(self):
        return self.ggirlnum
    girlnum.short_description = '女生数量'
    def boynum(self):
        return self.gboynum
    boynum.short_description = '男生数量'
    def isdelete(self):
        return self.isDelete
    isdelete.short_description = '是否删除'
    list_display = ['pk',name,gdatetime,girlnum,boynum,isdelete]
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5

    fieldsets = [
        ('数量',{'fields':['ggirlnum','gboynum']}),
        ('基本信息',{'fields':['gname','gdate','isDelete']})
    ]

@admin.register(Students)
class Studentadmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return '男'
        else:
            return '女'
    gender.short_description = '性别'
    def name(self):
        return self.sname
    name.short_description = '名字'
    def age(self):
        return self.sage
    age.short_description = '年龄'
    def content(self):
        return self.scontend
    content.short_description = '描述'
    def isdelete(self):
        return self.isDelete
    isdelete.short_description = '是否删除'
    def grade(self):
        return self.sgrade
    grade.short_description = '班级'
    list_display = ['pk', name, gender, age, content, isdelete,grade]
    search_fields = ['sname']
    list_per_page = 5


#admin.site.register(Grades,GradeAdmin)
#admin.site.register(Students)