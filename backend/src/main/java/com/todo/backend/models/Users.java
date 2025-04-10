package com.todo.backend.models;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;



@Document(collection="users")
public class Users {
    
    
    @Id
    private String id;
    private String userName;
    private String password;

    public Users() {
    }

    public Users(String id, String username, String password) {
        this.id = id;
        this.userName = username;
        this.password = password;
    }    

    public String getId() {
        return this.id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getUsername() {
        return this.userName;
    }

    public void setUsername(String username) {
        this.userName = username;
    }

    public String getPassword() {
        return this.password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    
}
