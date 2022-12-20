登录：

```javascript
//input
{
    username,
    password,
}
//output
#if status == 0, 无法登录
{
    success:True
	real_name：实际姓名
	username：用户名
	password：密码
	sex：性别
    status: 是否通过审核
    type: 可能是 学生/教师/校友
    type == "0":
    {
        school_name:
        grade:
        major:
    }
    type == "1":
    {
        profession_title
        research_direction
        lab_belonging
    }
    type == "2":
    {
        school_name
        work_field
        enterprise_belonging
    }
    type == "3":
    {
        
    }
}
{
    success:
    0 for wrong username / password
    1 for log in success
    2 for waiting for judge
}
```

注册：

```javascript
//input
{
    id
    real_name：实际姓名
	username：用户名
	password：密码
	sex：性别
    status: 是否通过审核(0)
    type
    学生/管理员/教师/校友的信息
}
//output
{
    success:
    0 for repeat username
    1 for register successful
}
```



修改个人信息：

```js
//input
{
    id
    real_name
    username
    //没有密码！！！
    sex
    type
    学生/管理员/教师/校友的信息
}
//output
//替换全部信息
{
    success
}
```

修改密码：

```js
//input
{
    id
    password
}
//output
#change the password
{
    success
}
```





创建简历：

```js
//input
{
    id
    sender
    name
    edu_background
    per_statement
    experience
}
//output
{
    success
}
```

投递简历：

```js
//input
{
    id (sender+receiver)
    resume(sender+name)
    receiver(username)
}
//output
{
    success
}
```

查看收到的简历：

```js
//input
{
    receiver(username)
}
//output
{
    resumes: [resume.receiver == receiver]
}
```

查看我的简历

```js
//input
{
    sender
}
//output
{
    resumes: [resume.sender == sender]
}
```

接收简历

```js
//input
{
	id,
    status //1 or 2
}
//output
#change resume.status = status
{
	success   
}
```

删除简历

```js
//input
{
    id
}
//output
#delete resume if resume.id = id
{
    success
}
```





创建岗位

```js
//input
{
    id 
    name
    pospublisher
    description
    demanding
    salary
    place
    label1
    label2
    label3
}
//output
{
    success
}
```

查询岗位

```js
//input
{
    label1
    label2
    label3
    salary
    place
}
//output
[
{
    id 
    name
    pospublisher
    description
    demanding
    salary
    place
}
]
```

删除岗位

```js
//input
{
    id
}
//output
#delete position if position.id = id
{
    success
}
```





管理员部分

查看注册信息：

```js
//input
{}
//output
[
    user if user.status == 0
]
```

通过注册：

```js
//input
{
    username
}
//output
# change user.status = 1
{
    success
}
```

删除注册：

```js
//input
{
    username
}
//output
# delete user if user.username == username
{
    success
}
```



帖子部分

发布帖子：

```js
//input
{
    id (title)
    title
  	content
}
//output
{
    success 
    0 for repeat title
    1 for successful add
}
```

查看帖子：

```js
//input
{}
//output
[
    {
        id
        title
        content
    }
]
```

删除帖子：

```js
//input
{
    id
}
//output
#delete issue if issue.id == id
{
    success
}
```

