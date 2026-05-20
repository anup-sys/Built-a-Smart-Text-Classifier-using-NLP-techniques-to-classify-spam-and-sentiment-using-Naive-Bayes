package org.example.autowireddemo1;

import org.springframework.stereotype.Service;

@Service
public class StudentService1 {

    public String getStudentMessage() {
        return "Student Service Running";
    }
}
