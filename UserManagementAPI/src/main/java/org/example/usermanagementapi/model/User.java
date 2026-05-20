package org.example.usermanagementapi.model;

public class user {
    private int id;
    private String name;

    public user(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public int getId() { return id; }
    public String getName() { return name; }
}
