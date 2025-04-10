package com.todo.backend.repositories;
import org.springframework.data.mongodb.repository.MongoRepository;
import com.todo.backend.models.Users;

public interface UsersRepo extends MongoRepository<Users, String>{
    
    public Users findByUserName(String userName);

}
