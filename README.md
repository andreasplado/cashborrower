# noortemaja

#### Event handling system for cashborrower.

This site is made in python for educational purpouses.




Main classes:
* models.py
* views.py
* serializers.py

###How To continue developing

First make Make data serializer

```
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        #fields =('comment')
        fields = '__all__'
```

Then make view. Don't forget to use pagination. It is really important for lazyloading data in my app.
You can only use Pagination class inside generics.

Example:

```
class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        post_fk = self.kwargs['post_fk']
        return Comment.objects.filter(loan=loan_fk)

Then path to url-s with foreign key.
```
Then add CommentListView inside urls. The view must use .as_view. This way you can call generics view.

```
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^loans/$', views.LoanListView.as_view()),
    url(r'^loan/(?P<id>[0-9]+)', views.LoanDetailAPIView.as_view()),
    url(r'^loan/update/(?P<id>[0-9]+)/', views.LoanUpdateAPIView.as_view()),
    url(r'^loan/delete/(?P<id>[0-9]+)', views.LoanDeleteAPIView.as_view()),

    url(r'^loancomments/loan/(?P<loan_fk>[0-9]+)', views.CommentListView.as_view()),
    url(r'^loancomment/loan/(?P<loan_fk>[0-9]+)/comment/(?P<id>[0-9]+)', views.CommentDetailAPIView.as_view()),
    url(r'^loancomment/update/loan/(?P<loan_fk>[0-9]+)/comment/(?P<id>[0-9]+)', views.CommentUpdateAPIView.as_view()),
    url(r'^loancomment/delete/loan/(?P<loan_fk>[0-9]+)/comment/(?P<id>[0-9]+)', views.CommentDeleteAPIView.as_view()),
]


```











To refresh the site use pareload in pythoneverywhere console of just click the refresh site button ;)



###How to refresh site after updates

You need to use https://github.com/ayys/pareload

###How To Use pareload

```
cd pareload
./pareload

```
You can run 
    ```
    pa-refresh
    ``` from anywhere to refresh the webapp

###Need Help?
To make user for the event handling system please contact with the repository owner andreasplado@gmail.com
