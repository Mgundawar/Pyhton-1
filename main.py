from user import User
from post import Post

app_user_one = User("mg@gmail.com", "Manoj Gundawar", "pwd", "Manager")
app_user_one.get_user_info()

app_user_two = User("pals@yahoo.com", "Pallavi G", "", "Tech lead")
app_user_two.get_user_info()

new_post = Post("Finishing project today", app_user_two.name)
new_post.get_post_info()
