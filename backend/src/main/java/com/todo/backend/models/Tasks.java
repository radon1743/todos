package com.todo.backend.models;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection="tasks")
public class Tasks {

    @Id
    private String taskId;
    private String date;
    private String text;
    private Boolean isCompleted;


    public Tasks() {
    }

    public Tasks(String id, String taskId, String date, String text, boolean isCompleted) {
       
        this.taskId = taskId;
        this.date = date;
        this.text = text;
        this.isCompleted = isCompleted;
    }

    public String getTaskId() {
        return this.taskId;
    }

    public void setTaskId(String taskId) {
        this.taskId = taskId;
    }

    public String getDate() {
        return this.date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public String getText() {
        return this.text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public Boolean isIsCompleted() {
        return this.isCompleted;
    }

    public Boolean getIsCompleted() {
        return this.isCompleted;
    }

    public void setIsCompleted(Boolean isCompleted) {
        this.isCompleted = isCompleted;
    }
    
}
