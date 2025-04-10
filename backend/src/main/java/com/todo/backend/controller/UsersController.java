package com.todo.backend.controller;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.todo.backend.models.Users;
import com.todo.backend.service.users.UsersService;

@RestController
@RequestMapping("/api")
public class UsersController {

    @Autowired
    private UsersService usersService;

    @GetMapping("/findAllUsers")
    public ResponseEntity<List<Users>> getUser() {

        List<Users> users = usersService.getAllUsers();
        return ResponseEntity.ok(users);
    }
}
