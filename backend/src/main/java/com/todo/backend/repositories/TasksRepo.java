package com.todo.backend.repositories;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import com.todo.backend.models.Tasks;

@Repository
public interface TasksRepo extends MongoRepository<Tasks, String>{
    Tasks findByTaskId(String taskId);
}
