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

        if len(user) != 0:
            db_password = user[0][3]
            status = user[0][5]
            if status == "0":
                response['success'] = 2
                # waiting for judge
                return Response(response)
            if password == db_password:
                response['success'] = 1

                response['id'] = user[0][0]
                response['username'] = user[0][1]
                response['real_name'] = user[0][2]
                response['password'] = user[0][3]
                response['sex'] = user[0][4]
                response['status'] = user[0][5]
                response['type'] = user[0][6]
                db_type = user[0][6]

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
                    response['lab_belonging_id'] = teacher[0][3]
                    return Response(response)
                elif db_type == "2":
                    schoolMate = sql.findSchoolMate(username)
                    response['school_name'] = schoolMate[0][1]
                    response['work_field'] = schoolMate[0][2]
                    response['enterprise_belonging_id'] = schoolMate[0][3]
                    return Response(response)
                else:
                    # db_type == "3"
                    return Response(response)

            else:
                # password wrong
                response['success'] = 0
                return Response(response)

        else:
            # username wrong
            response['success'] = 0
            return Response(response)

'''
class Login(APIView):
    def get(self, request):
        username = request.GET.get('username')
        password = request.GET.get('password')

        user = sql.findUser(username)
        response = dict()

        if len(user) != 0:
            db_password = user[0][3]
            status = user[0][5]
            if status == "0":
                response['success'] = 2
                # waiting for judge
                return Response(response)
            if password == db_password:
                response['success'] = 1
                return Response(response)
            else:
                # password wrong
                response['success'] = 0
                return Response(response)

        else:
            # username wrong
            response['success'] = 0
            return Response(response)
'''

class Register(APIView):
    def get(self, request):
        id = request.GET.get('id')
        username = request.GET.get('username')
        real_name = request.GET.get('real_name')
        password = request.GET.get('password')
        sex = request.GET.get('sex')
        type = request.GET.get('type')
        status = "0"

        user = sql.findUser(id)

        if len(user) == 0:
            if type == "0":
                school_name = request.GET.get('school_name')
                grade = request.GET.get('grade')
                major = request.GET.get('major')
                sql.createStudent(id, username, real_name, password, sex, type, school_name, grade, major, status)
            elif type == "1":
                profession_title = request.GET.get('profession_title')
                lab_belonging_id = request.GET.get('lab_belonging_id')
                research_direction = request.GET.get('research_direction')
                sql.createTeacher(id, username, real_name, password, sex, type,
                                  profession_title, lab_belonging_id, research_direction, status)
            elif type == "2":
                school_name = request.GET.get('school_name')
                work_field = request.GET.get('work_field')
                enterprise_belonging_id = request.GET.get('enterprise_belonging_id')
                sql.createSchoolMate(id, username, real_name, password, sex, type,
                                     school_name, work_field, enterprise_belonging_id, status)

            elif type == "3":
                sql.createAdminer(id, username, real_name, password, sex, type, status)

            return Response({'success': 1})
        else:
            return Response({'success': 0})


class LookInfo(APIView):
    def get(self, request):
        id = request.GET.get('id')

        user = sql.findUser(id)
        response = dict()

        response['username'] = user[0][1]
        response['real_name'] = user[0][2]
        response['password'] = user[0][3]
        response['sex'] = user[0][4]
        response['status'] = user[0][5]
        response['type'] = user[0][6]
        db_type = user[0][6]

        if db_type == "0":
            student = sql.findStudent(id)
            response['school_name'] = student[0][1]
            response['grade'] = student[0][2]
            response['major'] = student[0][3]
            return Response(response)
        elif db_type == "1":
            teacher = sql.findTeacher(id)
            response['profession_title'] = teacher[0][1]
            response['research_direction'] = teacher[0][2]
            response['lab_belonging_id'] = teacher[0][3]
            return Response(response)
        elif db_type == "2":
            schoolMate = sql.findSchoolMate(id)
            response['school_name'] = schoolMate[0][1]
            response['work_field'] = schoolMate[0][2]
            response['enterprise_belonging_id'] = schoolMate[0][3]
            return Response(response)
        else:
            # db_type == "3"
            return Response(response)


class UpdateInfo(APIView):
    def get(self, request):
        id = request.GET.get('id')
        real_name = request.GET.get('real_name')
        sex = request.GET.get('sex')

        user = sql.findUser(id)
        type = user[0][6]

        if type == "0":
            school_name = request.GET.get('school_name')
            grade = request.GET.get('grade')
            major = request.GET.get('major')
            sql.updateStudentInfo(id, real_name, sex, school_name, grade, major)
        elif type == "1":
            profession_title = request.GET.get('profession_title')
            research_direction = request.GET.get('research_direction')
            lab_belonging_id = request.GET.get('lab_belonging_id')
            sql.updateTeacherInfo(id, real_name, sex, profession_title, research_direction, lab_belonging_id)
        elif type == "2":
            school_name = request.GET.get('school_name')
            work_field = request.GET.get('work_field')
            enterprise_belonging_id = request.GET.get('enterprise_belonging_id')
            sql.updateSchoolMateInfo(id, real_name, sex, school_name, work_field, enterprise_belonging_id)
        else:
            sql.updateAdminerInfo(id, real_name, sex)
        return Response({'success': True})


class ChangePassword(APIView):
    def get(self, request):
        id = request.GET.get('id')
        password = request.GET.get('password')
        sql.updatePassword(id, password)
        return Response({'success': True})


class MakeResume(APIView):
    def get(self, request):
        id = request.GET.get('id')

        resume = sql.findResume(id)

        if len(resume) == 0:
            sender_id = request.GET.get('sender_id')
            name = request.GET.get('name')
            edu_background = request.GET.get('edu_background')
            per_statement = request.GET.get('per_statement')
            experience = request.GET.get('experience')
            status = "0"
            sql.createResume(id, name, edu_background, per_statement, experience, status, sender_id)
            return Response({'success': True})
        else:
            return Response({'success': False})


class SendResume(APIView):
    def get(self, request):
        position_id = request.GET.get('position_id')

        resumes = sql.findResumeByPosition(position_id)

        if len(resumes) == 0:
            resume_id = request.GET.get('resume_id')
            sql.positionGetResume(position_id, resume_id)
            return Response({'success': True})
        else:
            return Response({'success': False})


class LookReceiveResume(APIView):
    def get(self, request):
        receiver_id = request.GET.get('receiver')

        resumes = sql.findReceivedResumes(receiver_id)

        response = []

        length = len(resumes)
        i = 0
        while i < length:
            response.append({'id': resumes[i][0], 'name': resumes[i][1],
                             'edu_background': resumes[i][2], 'per_statement': resumes[i][3],
                             'status': resumes[i][3], 'sender_id': resumes[i][4], 'position_name': resumes[i][5]})
            i += 1

        return Response(response)


class LookMyResume(APIView):
    def get(self, request):
        sender_id = request.GET.get('sender')

        resumes = sql.findMyResumes(sender_id)

        response = []

        length = len(resumes)
        i = 0
        while i < length:
            response.append({'id': resumes[i][0], 'name': resumes[i][1],
                             'edu_background': resumes[i][2], 'per_statement': resumes[i][3],
                             'status': resumes[i][3], 'sender_id': resumes[i][4]})
            i += 1

        return Response(response)


class ChangeResumeStatus(APIView):
    def get(self, request):
        status = request.GET.get('status')
        id = request.GET.get('id')

        sql.updateResumeStatus(id, status)

        return Response({'success': True})


class DeleteResume(APIView):
    def get(self, request):
        id = request.GET.get('id')

        sql.deleteResume(id)

        return Response({'success': True})


class CreatePosition(APIView):
    def get(self, request):
        id = request.GET.get('id')
        name = request.GET.get('name')
        posPublisher_id = request.GET.get('posPublisher_id')
        description = request.GET.get('description')
        demanding = request.GET.get('demanding')
        salary = request.GET.get('salary')
        place = request.GET.get('place')
        label1 = request.GET.get('label1')
        label2 = request.GET.get('label2')
        label3 = request.GET.get('label3')

        sql.createPosition(id, name, description, demanding, salary, posPublisher_id, place, label1, label2, label3)

        return Response({'success': True})


class SearchPosition(APIView):
    def get(self, request):
        label1 = request.GET.get('label1')
        label2 = request.GET.get('label2')
        label3 = request.GET.get('label3')
        salary = request.GET.get('salary')
        place = request.GET.get('place')

        positionSet = set(sql.findAllPosition())
        if label1 != "":
            positionSet = positionSet.intersection(set(sql.findPositionWithLabel1(label1)))
        if label2 != "":
            positionSet = positionSet.intersection(set(sql.findPositionWithLabel2(label2)))
        if label3 != "":
            positionSet = positionSet.intersection(set(sql.findPositionWithLabel3(label3)))
        if salary != "":
            positionSet = positionSet.intersection(set(sql.findPositionWithSalary(salary)))
        if place != "":
            positionSet = positionSet.intersection(set(sql.findPositionWithPlace(place)))

        response = []

        for p in positionSet:
            response.append({'id': p[0], 'name': p[1], 'description': p[2], 'demanding': p[3], 'salary': p[4], 'place': p[5]})

        return Response(response)


class SearchMySendPosition(APIView):
    def get(self, request):
        posPublisher_id = request.GET.get('posPublisher_id')

        positions = sql.findPositionWithPosPublisherId(posPublisher_id)

        response = []
        for p in positions:
            response.append({'id': p[0], 'name': p[1], 'description': p[2], 'demanding': p[3], 'salary': p[4],
                             'place': p[5], 'label1': p[6], 'label2': p[7], 'label3': p[8]})
        return Response(response)


class DeletePosition(APIView):
    def get(self, request):
        id = request.GET.get('id')

        sql.deletePosition(id)

        return Response({'success': True})


class LookRegisterInfo(APIView):
    def get(self, request):
        user = sql.findWaitingRegister()

        response = []

        for u in user:
            response.append({'id': u[0], 'username': u[1], 'real_name': u[2], 'password': u[3], 'sex': u[4], 'status': u[5], 'type': u[6]})

        return Response(response)


class PassRegister(APIView):
    def get(self, request):
        username = request.GET.get('username')

        sql.updateUserStatus(username)

        return Response({'success': True})


class DeleteRegister(APIView):
    def get(self, request):
        username = request.GET.get('username')

        sql.deleteUser(username)

        return Response({'success': True})


class SendPost(APIView):
    def get(self, request):
        id = request.GET.get('id')
        title = request.GET.get('title')
        content = request.GET.get('content')
        if len(sql.findPost(id)) == 0:
            sql.createPost(id, title, content)
            return Response({'success': 1})
        else:
            return Response({'success': 0})


class LookPost(APIView):
    def get(self, request):
        post = sql.findAllPost()

        response = []

        for p in post:
            response.append(
                {'id': p[0], 'title': p[1], 'content': p[2]}
            )

        return Response(response)


class DeletePost(APIView):
    def get(self, request):
        id = request.GET.get('id')

        sql.deletePost(id)

        return Response({'success': True})


class StatisticUserType(APIView):
    def get(self, request):

