package com.todo.backend.service.tasks;


import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.todo.backend.models.Tasks;
import com.todo.backend.repositories.TasksRepo;

@Service
public class TasksServiceImpl implements TasksService{

    @Autowired
    public TasksRepo tasksRepo; 

    @Override
    public List<Tasks> getAllTasks(){
        return tasksRepo.findAll();
    }

    @Override
    public void addTask(Tasks task) {
        tasksRepo.insert(task);
    }

    @Override
    public void deleteTask(String id){
        tasksRepo.deleteById(id);
    }

    @Override 
    public Tasks getTask(String id){
        return tasksRepo.findByTaskId(id);
    
    }

    @Override 
    public Tasks editTask(String id, Tasks updatedTask){

        Tasks newTask = getTask(id);

        if(updatedTask.getIsCompleted() != null){
            newTask.setIsCompleted(updatedTask.getIsCompleted());
        }
        if(updatedTask.getDate() != null){
            newTask.setDate(updatedTask.getDate());

        }
        if(updatedTask.getText() != null){
            newTask.setText(updatedTask.getText());
        }
        return tasksRepo.save(newTask);
    }
}
