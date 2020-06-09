# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:46:45 2020

@author: de
"""
from django.http import HttpResponse
from django.shortcuts import render,redirect
from shopping.models import Books,Members,Carts,Orders

log_io=0
home_message=''
member=0

def home(request):
    global home_message
    return render(request,'home.html',{"home_message":home_message})


def account_create(request):
    if request.method == "POST":
        memberaccount=request.POST.get('memberaccount',None)
        memberpassword=request.POST.get('memberpassword',None)
        memberpasswordagain=request.POST.get('memberpasswordagain',None)
        membername=request.POST.get('membername',None)
        memberaddress=request.POST.get('memberaddress',None)
        memberphone=request.POST.get('memberphone',None)
        message = "所有字段都必须填写！"
        global member
        if memberaccount and memberpassword and membername and memberaddress and memberphone:
            same_member=Members.objects.filter(MemberAccount = memberaccount)
            if same_member:
                message="用户已存在，请重新输入账号！"
                return render(request, 'account_create.html', {"message": message})
            if memberpassword != memberpasswordagain:
                message='两次输入的密码不同！'
                return render(request, 'account_create.html', {"message": message})
            member=Members(
                MemberAccount=memberaccount,
                MemberPassword=memberpassword,
                MemberName=membername,
                MemberAddress=memberaddress,
                MemberPhone=memberphone)
            member.save()
            return redirect('/shopping_basket/')
        return render(request, 'account_create.html', {"message": message})
    return render(request,'account_create.html')


def login(request):
    if request.method == "POST":
        memberaccount = request.POST.get('memberaccount', None)
        memberpassword = request.POST.get('memberpassword', None)
        message = "所有字段都必须填写！"
        if memberaccount and memberpassword:  # 确保用户名和密码都不为空
            try:
                global member
                member = Members.objects.get(MemberAccount = memberaccount)
                if member.MemberPassword == memberpassword:
                    global home_message
                    home_message='尊贵的vip客户，欢迎回来！'
                    # orders=Orders.objects.filter(MemberAccount = member)
                    # books=[]
                    # for order in orders:
                    #     books.append(Books.objects.filter(ISBN = order.ISBN)[0])
                    # num=range(len(orders))
                    # for idx in num:
                    #     print(idx)
                    return redirect('/shopping_basket/')
                    # return render(request,'shopping_basket.html' ,{
                    #     "orders" : orders,
                    #     "books":books,
                    #     "num":num,
                    #     "home_message":home_message})
                    #return redirect('/shopping_basket/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'login.html', {"message": message})
    return render(request,'login.html')


def shopping_basket(request):
    global member
    orders=Orders.objects.filter(MemberAccount = member)
    return render(request,'shopping_basket.html',{"orders":orders})


def search(request):
    bookname=request.POST.get('bookname', None)
    bookauthor=request.POST.get('bookauthor', None)
    isbn=request.POST.get('isbn', None)   
    print(bookname,bookauthor,isbn) 
    books = Books.objects.all()
    if bookname:
        books=books.filter(BookName=bookname)
    if bookauthor:
        books=books.filter(BookAuthor=bookauthor)    
    if isbn:
        books=books.filter(ISBN=isbn)        
    return render(request,'search.html',
                  {'books':books})


def checkout(request):
    global member
    if member:
        return render(request,'checkout.html')
    else:
        global home_message
        home_message="用户未登录！"
        return render(request,"home.html",{'message':home_message})


def helpi(request):
    return render(request,'helpi.html')


def FAQ(request):
    return render(request,'FAQ.html')


def system(request):
    return render(request,'system.html')


def contact(request):
    return render(request,'contact.html')

def s_account(request):
    request.GET['username']
    request.GET['key']
    request.GET['email']
    return render(request,'s_account.html')

def logout(request):
    global member
    global home_message
    member=0
    home_message='用户未登录！'
    return redirect('..')