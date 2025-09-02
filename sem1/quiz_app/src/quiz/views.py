from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import transaction
from .models import Exam
from .forms import ExamForm, QuestionForm, ChoiceFormSet

def exam_list(request):
    exams = Exam.objects.all().order_by('-created_date')
    return render(request, 'quiz/exam_list.html', {'exams': exams})

def exam_detail(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    questions = exam.questions.all().prefetch_related('choices')
    return render(request, 'quiz/exam_detail.html', {'exam': exam, 'questions': questions})

def exam_create(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save()
            messages.success(request, 'Exam created.')
            return redirect('question_create', exam_id=exam.id)
    else:
        form = ExamForm()
    return render(request, 'quiz/exam_form.html', {'form': form})

def question_create(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if request.method == 'POST':
        qform = QuestionForm(request.POST)
        if qform.is_valid():
            with transaction.atomic():
                question = qform.save(commit=False)
                question.exam = exam
                question.save()
                formset = ChoiceFormSet(request.POST, instance=question)
                if formset.is_valid():
                    formset.save()
                    return redirect('exam_detail', exam_id=exam.id)
    else:
        qform = QuestionForm()
        formset = ChoiceFormSet()
    return render(request, 'quiz/question_form.html', {'exam': exam, 'question_form': qform, 'formset': formset})
