package com.todo.backend.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.todo.backend.models.Tasks;
import com.todo.backend.service.tasks.TasksService;



@RestController
@RequestMapping("/api")
public class TasksController {
    
    @Autowired
    private TasksService tasksService;

    @GetMapping("/findAllTasks")
    public ResponseEntity<List<Tasks>> getAllTasks() {
        List<Tasks> tasks = tasksService.getAllTasks();
        return ResponseEntity.ok(tasks);
    }

    @PostMapping("/addTasks")
    public String addTask(@RequestBody Tasks task) {
        tasksService.addTask(task);
        return "Added Successfully";
    }

    @DeleteMapping("/deleteTasks/{taskId}")
    public String deleteTask(@PathVariable String taskId) {
        tasksService.deleteTask(taskId);
        return "Deleted Successfully";
    }
    
}
