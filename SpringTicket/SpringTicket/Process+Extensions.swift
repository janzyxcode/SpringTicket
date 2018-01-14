//
//  Process+Extensions.swift
//  SpringTicket
//
//  Created by liaonaigang on 2018/1/14.
//  Copyright © 2018年 NG. All rights reserved.
//

import Foundation

extension Process{
    class func runTask(_ launchPath: String, _ arguments: [String]?){
        
        let task = Process()
        task.launchPath = launchPath
        task.arguments = arguments
        task.launch()
        
        //        let outpipe = Pipe()
        //        task.standardInput = outpipe
        //        let errpipe = Pipe()
        //        task.standardError = errpipe
        //
        //        outpipe.fileHandleForReading.readabilityHandler = {(handle) in
        //            let data = handle.readData(ofLength: 128)
        //            print("out:  " + String(data: data, encoding: String.Encoding.utf8)!)
        //        }
        //
        //        errpipe.fileHandleForReading.readabilityHandler = {(handle) in
        //            let data = handle.readData(ofLength: 128)
        //            print("error:  " + String(data: data, encoding: String.Encoding.utf8)!)
        //        }
    }
}
