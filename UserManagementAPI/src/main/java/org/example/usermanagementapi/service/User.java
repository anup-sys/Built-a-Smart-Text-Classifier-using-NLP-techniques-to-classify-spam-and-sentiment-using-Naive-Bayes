package org.example.usermanagementapi.service;

import org.apache.catalina.User;
import org.example.usermanagementapi.model.user;
import org.springframework.stereotype.service;

@Service
public class userservice {
    private List<user> users = new ArrayList<>();

    public List<user> getAllUsers() {
        return users;
    }

    public String adduser(User user) {
        users.add(user);
        return "User Added";
    }

    public user getuserById(int id) {
        return users.stream()
                .filter(u -> u.getId() == id)
                .findFirst()
                .orElse(null);
    }

    public String deleteuser(int id) {
        users.removeIf(u -> u.getId() == id);
        return "User Deleted";
    }
}
}
