登录：

```javascript
//input
{
    username,
    password,
}
//output
{
    success:True
	real_name：实际姓名
	username：用户名
	password：密码
	sex：性别
    type: 可能是 学生/教师/校友
    学生/管理员/教师/校友的信息 
}
{
    success:False
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
    type
    学生/管理员/教师/校友的信息
}
//output
{
    success: true/false 代表是否用户名重复
}
```

创建简历：

```js
//input
{
    id
    sender
    name
    content
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
    resume_id(sender+name)
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

