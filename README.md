# drf-project
### Basic Project to learn Django Rest Framework

***

## IMDB API Clone With DRF

1. Admin Access
* Admin Section: http://127.0.0.1:8000/dashboard/
<br>

2. Accounts
* Registration: http://127.0.0.1:8000/account/register/
* Login: http://127.0.0.1:8000/account/login/
* Logout: http://127.0.0.1:8000/account/logout/
<br>

3. Stream Platforms
* Create Element & Access List: http://127.0.0.1:8000/watch/stream/
* Access, Update & Destroy Individual Element: [http://127.0.0.1:8000/watch/&lt;int:movie_id&gt;/](http://127.0.0.1:8000/watch/stream/<int:streamplatform_id>/)
<br>

4. Watch List
* Create & Access List: http://127.0.0.1:8000/watch/
* Access, Update & Destroy Individual Element: [http://127.0.0.1:8000/watch/&lt;int:movie_id&gt;/](http://127.0.0.1:8000/watch/<int:movie_id>/)
<br>

5. Reviews
* Create Review For Specific Movie: [http://127.0.0.1:8000/watch/&lt;int:movie_id&gt;/reviews/create/](http://127.0.0.1:8000/watch/<int:movie_id>/reviews/create/)
* List Of All Reviews For Specific Movie: [http://127.0.0.1:8000/watch/&lt;int:movie_id&gt;/reviews/](http://127.0.0.1:8000/watch/<int:movie_id>/reviews/)
* Access, Update & Destroy Individual Review: [http://127.0.0.1:8000/watch/reviews/&lt;int:review_id&gt;/](http://127.0.0.1:8000/watch/reviews/<int:review_id>/)
<br>

6. User Review
* Access All Reviews For Specific User: http://127.0.0.1:8000/watch/user-reviews/?username=example
