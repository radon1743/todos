package com.todo.backend.service.users;

import java.util.List;

import com.todo.backend.models.Users;

public interface UsersService {
    public String test();
    public List<Users> getAllUsers();
    // public ResponseEntity<List<Users>> login();
}
