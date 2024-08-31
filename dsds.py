from flask import Flask, session, redirect, url_for, render_temple

def index():
    return "Hello"

app = Flask