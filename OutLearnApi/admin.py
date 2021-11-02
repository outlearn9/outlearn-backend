from django.contrib import admin
from .models.specialisationModel import *
from .models.higherStudyModel import *
from .models.tags import *
from .models.Course import *

# # Register your models here.
admin.site.register(Specialization,SpecializationAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(SpecializationWithCategory)
admin.site.register(Skill,SkillAdmin)
admin.site.register(HigherStudy,HigherStudyAdmin)
admin.site.register(Tags,TagAdmin)
admin.site.register(Courses,CourseAdmin)






