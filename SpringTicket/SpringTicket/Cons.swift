//
//  Cons.swift
//  SpringTicket
//
//  Created by liaonaigang on 2018/1/14.
//  Copyright © 2018年 NG. All rights reserved.
//

import Foundation

//let ProjectPath = "/Users/liaonaigang/Desktop/SprintTicket"
let ProjectPath = "/Users/user/Desktop/SpringTicket"
//let launchPath = ProjectPath + "/venv/bin/python3.5"
let launchPath = ProjectPath + "/venv1/bin/python3.6"
//let PythonDocmentPath = ProjectPath + "/Code/PythonFile"
let PythonDocmentPath = ProjectPath + "/PythonFile"
let updateTrainListPath = PythonDocmentPath + "/updatecTrainList.py"
let trainListPath = PythonDocmentPath + "/cons/trainList.json"
let configPath = PythonDocmentPath + "/cons/config.json"
let ticketLeftPath = PythonDocmentPath + "/tickets/ticketLeft.json"
let passengersPath = PythonDocmentPath + "/cons/passengers.json"

func getJson(_ path:String)->Any?{
    let mgr = FileManager.default
    if mgr.fileExists(atPath: path) {
        guard let content = mgr.contents(atPath: path) else{
            return nil
        }
        do {
            let json = try JSONSerialization.jsonObject(with: content, options: .mutableLeaves)
            return json
        }catch{
            print(error.localizedDescription)
        }
    }
    return nil
}
