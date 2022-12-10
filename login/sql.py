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


def createStudent(id, username, real_name, password, sex, type, school_name, grade, major):
    connection, cursor = connect_database()
    createUser(connection, cursor, id, username, real_name, password, sex, type)

    instruction = "insert into login_student(user_ptr_id, school_name, grade, major)" \
                  "values(%s,%s,%s,%s)"

    try:
        cursor.execute(instruction, [id,school_name,grade,major])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def createUser(connection, cursor, id, username, real_name, password, sex, type):
    instruction = "insert into login_user(id, username, real_name, password, sex, type) " \
                  "values(%s,%s,%s,%s,%s,%s)"

    try:
        cursor.execute(instruction, [id,username,real_name,password,sex,type])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")


def createPosPublisher(connection, cursor, id):
    instruction = "insert into login_pospublisher(user_ptr_id)" \
                  "values(%s)"

    try:
        cursor.execute(instruction, [id])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")


def createTeacher(id, username, real_name, password, sex, type, profession_title, lab_belonging_id, research_direction):
    connection, cursor = connect_database()
    createUser(connection, cursor, id, username, real_name, password, sex, type)
    createPosPublisher(connection, cursor, id)

    instruction = "insert into login_teacher(pospublisher_ptr_id, profession_title, lab_belonging_id, research_direction)" \
                  "values(%s,%s,%s,%s)"

    try:
        cursor.execute(instruction, [id, profession_title, lab_belonging_id, research_direction])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def createSchoolMate(id, username, real_name, password, sex, type, school_name, work_field, enterprise_belonging_id):
    connection, cursor = connect_database()
    createUser(connection, cursor, id, username, real_name, password, sex, type)
    createPosPublisher(connection, cursor, id)

    instruction = "insert into login_schoolmate(pospublisher_ptr_id, school_name, work_field, enterprise_belonging_id)" \
                  "values(%s,%s,%s,%s)"

    try:
        cursor.execute(instruction, [id, school_name, work_field, enterprise_belonging_id])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


def createAdminer(id, username, real_name, password, sex, type):
    connection, cursor = connect_database()
    createUser(connection, cursor, id, username, real_name, password, sex, type)

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


def createResume(id, name, content, sender_id):
    connection, cursor = connect_database()

    instruction = "insert into login_resume(id,name,content,sender_id)" \
                  "values(%s,%s,%s,%s)"

    try:
        cursor.execute(instruction, [id, name, content, sender_id])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

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


def findReceivedResumes(id):
    connection, cursor = connect_database()

    instruction = "select login_resume.* from login_resume, login_resume_receiver" \
                  "where login_resume.id=login_resume_receiver.resume_id and login_resume.id=%s"

    try:
        cursor.execute(instruction, [id])
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")
    result = cursor.fetchall()
    close_database(connection, cursor)

    return result

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


def createEnterprise(id, name, industry, place):
    connection, cursor = connect_database()

    instruction = "insert into login_enterprise(id,name,industry,place)" \
                  "values(%s,%s,%s,%s)"

    try:
        cursor.execute(instruction, [id,name,industry,place])
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


def createPosition(id, name, description, demanding, salary, posPublisher_id):
    connection, cursor = connect_database()

    instruction = "insert into login_position(id,name,description,demanding,salary,posPublisher_id)" \
                  "values(%s,%s,%s,%s,%s,%s)"

    try:
        cursor.execute(instruction, [id,name,description,demanding,salary,posPublisher_id])
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("执行MySQL错误")

    close_database(connection, cursor)


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