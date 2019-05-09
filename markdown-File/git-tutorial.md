# Git操作
一直想练习Git，今天终于有机会折腾了一下。导致commit十几次。:wink:这篇markdown权当做代码片段吧
## 登录
下载 git-bash后设置其全局的用户名和邮箱：
``` bash
git config --global user.name "Your name"
git config --global user.email "email@example.com"
```

## ssh-key生成
``` bash
ssh-keygen -t rsa -C "email@example.com"
```
ssh密钥添加到Github还有一个好处就是 push到远程仓库的时候 不用输入账户密码
## clone
``` bash
git clone git@github:username/repositories.git
```

## remote
```bash
git remote add origin git@github.com:YourName/repositories.git
```
## push
``` bash
git add fileName
git commit -m 'comment about this commit'
git push origin master
```

## pull
``` bash
git pull origin master
```