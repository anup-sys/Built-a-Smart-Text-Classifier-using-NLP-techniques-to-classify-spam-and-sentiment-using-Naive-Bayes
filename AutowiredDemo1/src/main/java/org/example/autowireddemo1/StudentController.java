package org.example.autowireddemo1;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class StudentController1 {

    @Autowired
    StudentService1 service1;

    @GetMapping("/student")
    public String showMessage() {
        return service1.getStudentMessage();
    }
}

