---
title: "Introduction to Apache Airflow"
speakers:
 - Jarek Potiuk
 - Tomasz Urbaszek
date: 2020-04-20T12:00:00
time_start: 2020-04-20T12:00:00
time_end: 2020-04-20T13:00:00
video: https://youtu.be/06tYjcQ12i4
slides: 
---

<p>Apache Airflow is a tool created by community to programmatically author, schedule and monitor workflows. The biggest advantage of Airflow is the fact that it does not limit the scope of pipelines. Airflow can be used for building Machine Learning models, transferring data or managing the infrastructure. Because Airflow workflows are written in pure Python, there is no restriction on what a single task can do. It can execute a python callable, bash script or create a new Kubernetes pod. Thanks to that, a single Airflow workflow can include tasks for both setup and teardown of external infrastructure, as well as operations that will be performed using the new resources.</p>

<p>During this talk Tomek Urbaszek and Jarek Potiuk, both Apache Airflow official committers, will provide an extensive introduction to Airflow, helping the audience understand the underlying concepts of Apache Airflow. They will also share best practices for developing workflows and provide a guide to when Airflow is the right choice and when other solutions should be considered.</p>