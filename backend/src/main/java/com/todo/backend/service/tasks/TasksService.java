package com.todo.backend.service.tasks;

import java.util.List;

import com.todo.backend.models.Tasks;


public interface TasksService {
    public List<Tasks> getAllTasks();
    public void addTask(Tasks task);
    public void deleteTask(String id);
}
