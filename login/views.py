from . import forms, models
from rest_framework.views import APIView
from rest_framework.response import Response
import login.sql as sql

# Create your views here.

class Login(APIView):
    def get(self, request):
        username = request.GET.get('username')
        password = request.GET.get('password')

        user = sql.findUser(username)
        response = dict()

        if user:
            db_password = user[0][3]
            response['success'] = True
            response['username'] = user[0][1]
            response['real_name'] = user[0][2]
            response['password'] = db_password
            response['sex'] = user[0][4]
            response['type'] = user[0][5]
            if password == db_password:
                db_type = user[0][5]
                if db_type == "0":
                    student = sql.findStudent(username)
                    response['school_name'] = student[0][1]
                    response['grade'] = student[0][2]
                    response['major'] = student[0][3]
                    return Response(response)
                elif db_type == "1":
                    teacher = sql.findTeacher(username)
                    response['profession_title'] = teacher[0][1]
                    response['research_direction'] = teacher[0][2]
                    response['lab_belonging'] = teacher[0][3]
                    return Response(response)
                elif db_type == "2":
                    schoolMate = sql.findSchoolMate(username)
                    response['school_name'] = schoolMate[0][1]
                    response['work_field'] = schoolMate[0][2]
                    response['enterprise_belonging_id'] = schoolMate[0][3]
                    return Response(response)
                elif db_type == "3":
                    return Response(response)
            else:
                return Response(response)

        else:
            response['success'] = False
            return Response(response)


class Register(APIView):
    def get(self, request):
        id = request.GET.get('id')
        username = request.GET.get('username')
        real_name = request.GET.get('real_name')
        password = request.GET.get('password')
        sex = request.GET.get('sex')
        type = request.GET.get('type')

        user = sql.findUser(id)

        if user:
            if type == "0":
                school_name = request.GET.get('school_name')
                grade = request.GET.get('grade')
                major = request.GET.get('major')
                sql.createStudent(id, username, real_name, password, sex, type, school_name, grade, major)
            elif type == "1":
                profession_title = request.GET.get('profession_title')
                lab_belonging_id = request.GET.get('lab_belonging_id')
                research_direction = request.GET.get('research_direction')
                sql.createTeacher(id, username, real_name, password, sex, type,
                                  profession_title, lab_belonging_id, research_direction)
            elif type == "2":
                school_name = request.GET.get('school_name')
                work_field = request.GET.get('work_field')
                enterprise_belonging_id = request.GET.get('enterprise_belonging_id')
                sql.createSchoolMate(id, username, real_name, password, sex, type,
                                     school_name, work_field, enterprise_belonging_id)

            elif type == "3":
                sql.createAdminer(id, username, real_name, password, sex, type)

            return Response({'success': True})
        else:
            return Response({'success': False})


class MakeResume(APIView):
    def get(self, request):
        id = request.GET.get('id')

        resume = sql.findResume(id)

        if len(resume) == 0:
            sender_id = request.GET.get('sender_id')
            name = request.GET.get('name')
            content = request.GET.get('content')
            sql.createResume(id, name, content, sender_id)
            return Response({'success': True})
        else:
            return Response({'success': False})


class SendResume(APIView):
    def get(self, request):
        id = request.GET.get('id')

        resume_receiver = sql.findResumeReceiver(id)

        if len(resume_receiver) == 0:
            resume_id = request.GET.get('resume_id')
            pospublisher_id = request.GET.get('pospublisher_id')
            sql.createResumeReceiver(id, resume_id, pospublisher_id)
            return Response({'success': True})
        else:
            return Response({'success': False})


class LookResume(APIView):
    def get(self, request):
        id = request.GET.get('receiver')

        resumes = sql.findReceivedResumes(id)

        response = []

        length = len(resumes)
        i = 0
        while i < length:
            response.append({'id': resumes[i][0], 'name': resumes[i][1],
                             'content': resumes[i][2], 'sender_id': resumes[i][3]})
            i += 1

        return Response(response)


