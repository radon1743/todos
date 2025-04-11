package com.todo.backend.controller;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.todo.backend.service.users.UsersService;



@RestController
@RequestMapping("/api")
public class BackendController {
    
    @Autowired
    private final UsersService backendService = null;

    @GetMapping("/test")
    public String getMethodName() {
        String s = backendService.test();
        System.out.println(s);
        return s;
    }

}
