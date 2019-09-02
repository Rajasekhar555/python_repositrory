from django.conf.urls import url, include
from django.contrib import admin


from .views import SchoolApp, students, teachers

urlpatterns = [

    url('', SchoolApp.home, name='home'),

    url('students/', include(([
        url('', students.QuizListView.as_view(), name='quiz_list'),
        url('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        url('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
        url('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
    ], 'SchoolApp'), namespace='students')),

    url('teachers/', include(([
        url('', teachers.QuizListView.as_view(), name='quiz_change_list'),
        url('quiz/add/', teachers.QuizCreateView.as_view(), name='quiz_add'),
        url('quiz/<int:pk>/', teachers.QuizUpdateView.as_view(), name='quiz_change'),
        url('quiz/<int:pk>/delete/', teachers.QuizDeleteView.as_view(), name='quiz_delete'),
        url('quiz/<int:pk>/results/', teachers.QuizResultsView.as_view(), name='quiz_results'),
        url('quiz/<int:pk>/question/add/', teachers.question_add, name='question_add'),
        url('quiz/<int:quiz_pk>/question/<int:question_pk>/', teachers.question_change, name='question_change'),
        url('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', teachers.QuestionDeleteView.as_view(), name='question_delete'),
    ], 'SchoolApp'), namespace='teachers')),
]