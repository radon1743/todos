package com.todo.backend.service.users;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.todo.backend.models.Users;
import com.todo.backend.repositories.UsersRepo;

@Service
public class UsersServiceImpl implements UsersService{
    
    @Autowired
    public UsersRepo usersRepo;

    @Override
    public String test(){
        return "test ok";
    }

    @Override
    public List<Users> getAllUsers(){
        return usersRepo.findAll();
    }
}
