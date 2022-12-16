import pymysql


def connect_database():
    connection = pymysql.connect(host="localhost",
                                 port=3306,
                                 db="blink_v0",
                                 user="root",
                                 passwd="paradise2002",
                                 charset="utf8")
    cursor = connection.cursor()
    return connection, cursor


def close_database(connection, cursor):
    connection.close()
    cursor.close()


def updateUserInfo(connection, cursor, id, real_name, sex):
    instruction = "update login_user" \
                  "set real_name=%s, sex=%s" \
                  "where id=%s"

    try:
        cursor.execute(instruction, [real_name,sex,id])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")


def updateStudentInfo(id, real_name, sex, school_name, grade, major):
    connection, cursor = connect_database()
    updateUserInfo(connection, cursor, id, real_name, sex)
    instruction = "update login_student" \
                  "set school_name=%s, grade=%s, major=%s" \
                  "where id=%s"

    try:
        cursor.execute(instruction, [school_name, grade, major, id])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def updateTeacherInfo(id, real_name, sex, profession_title, research_direction, lab_belonging_id):
    if findLab(lab_belonging_id):
        createLab(lab_belonging_id, lab_belonging_id)
    connection, cursor = connect_database()
    updateUserInfo(connection, cursor, id, real_name, sex)
    # 不用更新PosPublisher信息
    instruction = "update login_teacher" \
                  "set profession_title=%s, research_direction=%s, lab_belonging_id=%s" \
                  "where id=%s"

    try:
        cursor.execute(instruction, [profession_title, research_direction, lab_belonging_id, id])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def updateSchoolMateInfo(id, real_name, sex, school_name, work_field, enterprise_belonging_id):
    if findEnterprise(enterprise_belonging_id):
        createEnterprise(enterprise_belonging_id, enterprise_belonging_id, "None")
    connection, cursor = connect_database()
    updateUserInfo(connection, cursor, id, real_name, sex)
    # 不用更新PosPublisher信息
    instruction = "update login_schoolmate" \
                  "set school_name=%s, work_field=%s, enterprise_belonging_id=%s" \
                  "where id=%s"

    try:
        cursor.execute(instruction, [school_name, work_field, enterprise_belonging_id, id])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def updateAdminerInfo(id, real_name, sex):
    connection, cursor = connect_database()
    updateUserInfo(connection, cursor, id, real_name, sex)
    close_database(connection, cursor)


def updatePassword(id, password):
    connection, cursor = connect_database()
    instruction = "update login_user" \
                  "set password=%s" \
                  "where id=%s"

    try:
        cursor.execute(instruction, [id, password])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def findPosPublisher(posPublisher_id):
    connection, cursor = connect_database()
    instruction = "select * from login_pospublisher where user_ptr_id=%s"

    try:
        cursor.execute(instruction, [posPublisher_id])
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    result = cursor.fetchall()
    close_database(connection, cursor)
    return result


def findUser(user_id):
    connection, cursor = connect_database()
    instruction = "select * from login_user where id=%s"

    try:
        cursor.execute(instruction, [user_id])
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    result = cursor.fetchall()
    close_database(connection, cursor)
    return result


def findStudent(student_id):
    connection, cursor = connect_database()
    instruction = "select * from login_student where user_ptr_id=%s"

    try:
        cursor.execute(instruction, [student_id])
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    result = cursor.fetchall()
    close_database(connection, cursor)
    return result


def findTeacher(teacher_id):
    connection, cursor = connect_database()
    instruction = "select * from login_teacher where user_ptr_id=%s"

    try:
        cursor.execute(instruction, [teacher_id])
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    result = cursor.fetchall()
    close_database(connection, cursor)
    return result


def findSchoolMate(schoolMate_id):
    connection, cursor = connect_database()
    instruction = "select * from login_schoolmate where user_ptr_id=%s"

    try:
        cursor.execute(instruction, [schoolMate_id])
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    result = cursor.fetchall()
    close_database(connection, cursor)
    return result


def findAdminer(adminer_id):
    connection, cursor = connect_database()
    instruction = "select * from login_adminer where user_ptr_id=%s"

    try:
        cursor.execute(instruction, [adminer_id])
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    result = cursor.fetchall()
    close_database(connection, cursor)
    return result


def findLab(id):
    connection, cursor = connect_database()

    instruction = "select * from login_lab where id=%s"

    try:
        cursor.execute(instruction, [id])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    result = cursor.fetchall()
    close_database(connection, cursor)
    return result


def findEnterprise(id):
    connection, cursor = connect_database()

    instruction = "select * from login_enterprise where id=%s"

    try:
        cursor.execute(instruction, [id])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    result = cursor.fetchall()
    close_database(connection, cursor)
    return result


def createStudent(id, username, real_name, password, sex, type, school_name, grade, major, status):
    createUser(id, username, real_name, password, sex, type, status)
    connection, cursor = connect_database()

    instruction = "insert into login_student(user_ptr_id, school_name, grade, major)" \
                  "values(%s,%s,%s,%s)"

    try:
        cursor.execute(instruction, [id,school_name,grade,major])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def createUser(id, username, real_name, password, sex, type, status):
    connection, cursor = connect_database()
    instruction = "insert into login_user(id, username, real_name, password, sex, status, type) " \
                  "values(%s,%s,%s,%s,%s,%s,%s)"

    try:
        cursor.execute(instruction, [id,username,real_name,password,sex,status,type])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    close_database(connection, cursor)


def createPosPublisher(id):
    connection, cursor = connect_database()
    instruction = "insert into login_pospublisher(user_ptr_id)" \
                  "values(%s)"

    try:
        cursor.execute(instruction, [id])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    close_database(connection, cursor)


def createTeacher(id, username, real_name, password, sex, type, profession_title, lab_belonging_id, research_direction, status):
    if len(findLab(lab_belonging_id)) == 0:
        createLab(lab_belonging_id, lab_belonging_id)
    createUser(id, username, real_name, password, sex, type, status)
    createPosPublisher(id)
    connection, cursor = connect_database()


    instruction = "insert into login_teacher(pospublisher_ptr_id, profession_title, lab_belonging_id, research_direction)" \
                  "values(%s,%s,%s,%s)"

    try:
        cursor.execute(instruction, [id, profession_title, lab_belonging_id, research_direction])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def createSchoolMate(id, username, real_name, password, sex, type, school_name, work_field, enterprise_belonging_id, status):
    if len(findEnterprise(enterprise_belonging_id)) == 0:
        createEnterprise(id, id, "None")
    createUser(id, username, real_name, password, sex, type, status)
    createPosPublisher(id)
    connection, cursor = connect_database()

    instruction = "insert into login_schoolmate(pospublisher_ptr_id, school_name, work_field, enterprise_belonging_id)" \
                  "values(%s,%s,%s,%s)"

    try:
        cursor.execute(instruction, [id, school_name, work_field, enterprise_belonging_id])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def createAdminer(id, username, real_name, password, sex, type, status):
    createUser(id, username, real_name, password, sex, type, status)
    connection, cursor = connect_database()

    instruction = "insert into login_adminer(user_ptr_id)" \
                  "values(%s)"

    try:
        cursor.execute(instruction, [id])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def findResume(resume_id):
    connection, cursor = connect_database()

    instruction = "select * from login_resume where id=%s"

    try:
        cursor.execute(instruction, [resume_id])
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    result = cursor.fetchall()
    close_database(connection, cursor)
    return result


def findPositionWithPlace(place):
    connection, cursor = connect_database()

    instruction = "select * from login_position" \
                  "where place=%s"

    try:
        cursor.execute(instruction, [place])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    result = cursor.fetchall()
    close_database(connection, cursor)
    return result


def findPositionWithSalary(salary):
    connection, cursor = connect_database()

    instruction = "select * from login_position" \
                  "where salary=%s"

    try:
        cursor.execute(instruction, [salary])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    result = cursor.fetchall()
    close_database(connection, cursor)
    return result


def findPositionWithLabel3(label3):
    connection, cursor = connect_database()

    instruction = "select * from login_position" \
                  "where label2=%s"

    try:
        cursor.execute(instruction, [label3])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    result = cursor.fetchall()
    close_database(connection, cursor)
    return result


def findPositionWithLabel2(label2):
    connection, cursor = connect_database()

    instruction = "select * from login_position" \
                  "where label2=%s"

    try:
        cursor.execute(instruction, [label2])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    result = cursor.fetchall()
    close_database(connection, cursor)
    return result


def updateUserStatus(id):
    connection, cursor = connect_database()

    instruction = "update login_user" \
                  "set status=%s" \
                  "where id=%s"

    try:
        cursor.execute(instruction, ["1", id])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    close_database(connection, cursor)


def deleteUser(id):
    connection, cursor = connect_database()

    instruction = "delete from login_user" \
                  "where id=%s"

    try:
        cursor.execute(instruction, [id])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    close_database(connection, cursor)


def findPositionWithLabel1(label1):
    connection, cursor = connect_database()

    instruction = "select * from login_position" \
                  "where label1=%s"

    try:
        cursor.execute(instruction, [label1])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    result = cursor.fetchall()
    close_database(connection, cursor)
    return result


def findAllPosition():
    connection, cursor = connect_database()

    instruction = "select * from login_position"

    try:
        cursor.execute(instruction)
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    result = cursor.fetchall()
    close_database(connection, cursor)
    return result


def findAllPost():
    connection, cursor = connect_database()

    instruction = "select * from login_post"

    try:
        cursor.execute(instruction)
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    result = cursor.fetchall()
    close_database(connection, cursor)
    return result


def findPost(id):
    connection, cursor = connect_database()

    instruction = "select * from login_post" \
                  "where id=%s"

    try:
        cursor.execute(instruction, [id])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    result = cursor.fetchall()
    close_database(connection, cursor)
    return result



def createResume(id, name, edu_background, per_statement, experience, status, sender_id):
    connection, cursor = connect_database()

    instruction = "insert into login_resume(id,name,edu_background,per_statement,experience,status,sender_id)" \
                  "values(%s,%s,%s,%s,%s,%s,%s)"

    try:
        cursor.execute(instruction, [id, name, edu_background, per_statement, experience, status, sender_id])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def deletePosition(id):
    connection, cursor = connect_database()

    instruction = "delete from login_position where id=%s"

    try:
        cursor.execute(instruction, [id])
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    close_database(connection, cursor)


def deletePost(id):
    connection, cursor = connect_database()

    instruction = "delete from login_post where id=%s"

    try:
        cursor.execute(instruction, [id])
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    close_database(connection, cursor)


def findWaitingRegister():
    connection, cursor = connect_database()
    status = "0"
    instruction = "select * from login_user where status=%s"

    try:
        cursor.execute(instruction, [status])
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    result = cursor.fetchall()
    close_database(connection, cursor)


def findResumeReceiver(resume_receiver_id):
    connection, cursor = connect_database()

    instruction = "select * from login_resume_receiver where id=%s"

    try:
        cursor.execute(instruction, [resume_receiver_id])
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    result = cursor.fetchall()
    close_database(connection, cursor)

    return result


def createResumeReceiver(id, resume_id, receiver_id):
    connection, cursor = connect_database()

    instruction = "insert into login_resume_receiver(id,resume_id,receiver_id)" \
                  "values(%s,%s,%s)"

    try:
        cursor.execute(instruction, [id, resume_id, receiver_id])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def findReceivedResumes(receiver_id):
    connection, cursor = connect_database()

    instruction = "select login_resume.* from login_resume, login_resume_receiver" \
                  "where login_resume.id=login_resume_receiver.resume_id and login_resume.receiver_id=%s"

    try:
        cursor.execute(instruction, [receiver_id])
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    result = cursor.fetchall()
    close_database(connection, cursor)

    return result


def findMyResumes(sender_id):
    connection, cursor = connect_database()

    instruction = "select * from login_resume" \
                  "where sender_id=%s"

    try:
        cursor.execute(instruction, [sender_id])
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    result = cursor.fetchall()
    close_database(connection, cursor)

    return result


def updateResumeStatus(id, status):
    connection, cursor = connect_database()

    instruction = "update login_resume" \
                  "set status=%s" \
                  "where id=%s"

    try:
        cursor.execute(instruction, [status, id])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def deleteResume(id):
    connection, cursor = connect_database()
    instruction = "delete from login_resume" \
                  "where id=%s"

    try:
        cursor.execute(instruction, [id])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def createLab(id, name):
    connection, cursor = connect_database()

    instruction = "insert into login_lab(id,name)" \
                  "values(%s,%s)"

    try:
        cursor.execute(instruction, [id,name])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def createEnterpriseOnlyId(id, name):
    connection, cursor = connect_database()

    instruction = "insert into login_enterprise(id,name)" \
                  "values(%s,%s)"

    try:
        cursor.execute(instruction, [id,name])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def createEnterprise(id, name, industry):
    connection, cursor = connect_database()

    instruction = "insert into login_enterprise(id,name,industry)" \
                  "values(%s,%s,%s)"

    try:
        cursor.execute(instruction, [id,name,industry])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def clearAdminer():
    connection, cursor = connect_database()

    instruction = "delete from login_adminer;"

    try:
        cursor.execute(instruction)
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def clearEnterprise():
    connection, cursor = connect_database()

    instruction = "delete from login_enterprise;"

    try:
        cursor.execute(instruction)
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def clearLab():
    connection, cursor = connect_database()

    instruction = "delete from login_lab;"

    try:
        cursor.execute(instruction)
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def clearPosition():
    connection, cursor = connect_database()

    instruction = "delete from login_position;"

    try:
        cursor.execute(instruction)
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def clearPosPublisher():
    connection, cursor = connect_database()

    instruction = "delete from login_pospublisher;"

    try:
        cursor.execute(instruction)
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def clearPost():
    connection, cursor = connect_database()

    instruction = "delete from login_post;"

    try:
        cursor.execute(instruction)
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def clearResume():
    connection, cursor = connect_database()

    instruction = "delete from login_resume;"

    try:
        cursor.execute(instruction)
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def clearResumeReceiver():
    connection, cursor = connect_database()

    instruction = "delete from login_resume_receiver;"

    try:
        cursor.execute(instruction)
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def clearSchoolMate():
    connection, cursor = connect_database()

    instruction = "delete from login_schoolmate;"

    try:
        cursor.execute(instruction)
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def clearStudent():
    connection, cursor = connect_database()

    instruction = "delete from login_student;"

    try:
        cursor.execute(instruction)
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def clearTeacher():
    connection, cursor = connect_database()

    instruction = "delete from login_teacher;"

    try:
        cursor.execute(instruction)
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def clearUser():
    connection, cursor = connect_database()

    instruction = "delete from login_user;"

    try:
        cursor.execute(instruction)
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def createPost(id, title, content):

    connection, cursor = connect_database()

    instruction = "insert into login_post(id,title,content)" \
                  "values(%s,%s,%s)"

    try:
        cursor.execute(instruction, [id,title,content])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)




def createPosition(id, name, description, demanding, salary, posPublisher, place, label1, label2, label3):

    connection, cursor = connect_database()

    instruction = "insert into login_position(id,name,description,demanding,salary,posPublisher_id,place,label1,label2,label3)" \
                  "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    try:
        cursor.execute(instruction, [id,name,description,demanding,salary,posPublisher,place,label1,label2,label3])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def createUserIdOnly(id, username):
    createUser(id, username, "none", "none", "male", "none", "0")

def createPosPublisherIdOnly(id):
    createPosPublisher(id)


if __name__ == "__main__":
    clearResumeReceiver()
    clearResume()
    clearPosition()
    clearStudent()
    clearTeacher()
    clearSchoolMate()
    clearPosPublisher()
    clearAdminer()
    clearUser()
    clearEnterprise()
    clearLab()
    clearPost()
    createUserIdOnly("wh", "wh")
    createPosPublisherIdOnly("wh")

    createUserIdOnly("cjj", "cjj")
    createPosPublisherIdOnly("cjj")
    createPosition('wh-work', 'work', 'to be wh xiaodi', 'male', '1234', 'wh', 'beijing', '1', '2', '')
    createPosition('cjj-work', 'work', 'to be cjj baobiao', 'female', '5678', 'cjj', 'sh', '1', '', '')
    rst = findAllPosition()
    print(rst)
'''
    for i in range(5):
        createLab("lab"+str(i), "lab"+str(i))
        createEnterprise("enterprise"+str(i), "enterprise"+str(i), "CS", "Beijing")

    createStudent("lsz",'lsz','lsz','lsz250','male','0','THU','l_three','rap')
    createStudent("wxz", "wxz", "wxz", "wxz777", "male", "0", "BUAA", "l_three", "cs")

    createTeacher('wh','wh','wh','wh666','female','1','fujiaoshou','lab0','cs')
    createTeacher('lr','lr','lr','lr666','male','1','jiaoshou','lab1','db')

    createSchoolMate('cjj','cjj','cjj','cjj666','male','2','MIT','cs','enterprise0')
    createSchoolMate('qs','qs','qs','qs666','male','2','Oxford','cs','enterprise1')

    createAdminer('zfy','zfy','zfy','zfy666','male','3')

    createPosition('wh-work', 'work', 'to be wh xiaodi', 'male', '1234', 'wh')
    createPosition('cjj-work', 'work', 'to be cjj baobiao', 'female', '5678', 'cjj')

    createResume('lsz-xiaodi', 'xiaodi', 'want to be wh xiaodi', 'lsz')
    createResume('lsz-baobiao', 'baobiao', 'want to be cjj baobiao', 'lsz')

    createResumeReceiver('lsz-xiaodi-wh', 'lsz-xiaodi', 'wh')
    createResumeReceiver('lsz-baobiao-cjj', 'lsz-baobiao', 'cjj')

    result = findUser('fff')
    print(result)
'''