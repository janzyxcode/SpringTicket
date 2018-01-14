//
//  ViewController.swift
//  SpringTicket
//
//  Created by liaonaigang on 2018/1/13.
//  Copyright © 2018年 NG. All rights reserved.
//

import Cocoa


class ViewController: NSViewController {
    @IBOutlet weak var dateTableview: NSTableView!
    var dateArray = [String]()
    var selectedDateDic = [String: Int]()
    var selectedTrainDic = [String: Int]()
    var selectedPassengerDic = [String: Int]()
    var statusBtn:NSStatusItem?
    var popover:NSPopover?
    
    @IBOutlet weak var fromStationT: NSTextField!
    @IBOutlet weak var toStationT: NSTextField!
    @IBOutlet weak var personTableView: NSTableView!
    @IBOutlet weak var trainListTableView: NSTableView!
    @IBOutlet weak var tipL: NSTextField!
    @IBOutlet var selectedTextv: NSTextView!
    var trainList = [[String:Any]]()
    var passengerList = [[String:Any]]()
    @IBOutlet var passengerTextV: NSTextView!
    @IBOutlet var selectedTrainV: NSTextView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        settupviews()
        setDateArray()
        uploadInfo()
        
        NotificationCenter.default.addObserver(self, selector: #selector(taskTerminated(_:)), name: Process.didTerminateNotification, object: nil)
        
    }
    
    @objc func taskTerminated(_ noti:NSNotification){
        if let task = noti.object as? Process,
            let path = task.arguments?.first{
            if path == updateTrainListPath {
                getTrainList()
            }
        }
    }
    
    func setDateArray(){
        let dateFormat = DateFormatter()
        dateFormat.dateFormat = "yyyy-MM-dd"
        for item in 0..<30{
            let date = Date(timeIntervalSinceNow: TimeInterval(item * 24 * 60 * 60))
            dateArray.append(dateFormat.string(from: date))
        }
        dateTableview.reloadData()
    }
    
    @IBAction func updateTrainList(_ sender: Any) {
       Process.runTask(launchPath, [updateTrainListPath])
    }
    
    @IBAction func Save(_ sender: Any) {
        let url = configPath
        do {
            
            guard var dict = getJson(url) as? [String: Any] else{
                return
            }
            dict["出发地"] = fromStationT.stringValue
            dict["目的地"] = toStationT.stringValue
            dict["刷新日期"] = getSelectedStr(selectedDateDic.keys)
            
            let data = try JSONSerialization.data(withJSONObject: dict, options: .prettyPrinted)
            if let dataStr = NSString(data: data, encoding: String.Encoding.utf8.rawValue){
                try dataStr.write(toFile: url, atomically: false, encoding: String.Encoding.utf8.rawValue)
                tipL.stringValue = "保存成功"
            }
        }catch{
            tipL.stringValue = error.localizedDescription
        }
    }
    
    @IBAction func showUserInfo(_ sender: Any) {
        statusBtnAction((statusBtn!.button)!)
    }
}

extension ViewController{
    func settupviews(){
        popover = NSPopover()
        popover?.behavior = .transient
        popover?.appearance = NSAppearance(named:NSAppearance.Name.vibrantLight)
        popover?.contentViewController = MainViewController(nibName: NSNib.Name(rawValue: "MainViewController"), bundle: nil)
        
        statusBtn = NSStatusBar.system.statusItem(withLength: 30)
        let image = NSImage(named: NSImage.Name(rawValue: "train_ico"))
        image?.isTemplate = true
        statusBtn?.image = image
        statusBtn?.highlightMode = true
        statusBtn?.target = self
        statusBtn?.action = #selector(statusBtnAction(_:))
    }
    
    @objc func statusBtnAction(_ sender:NSView){    popover?.show(relativeTo: sender.bounds, of: sender, preferredEdge: NSRectEdge.maxY)
    }
}

extension ViewController:NSTableViewDelegate,NSTableViewDataSource{
    func numberOfRows(in tableView: NSTableView) -> Int {
        var count = 0
        if tableView === dateTableview {
            count = dateArray.count
        }else if tableView === trainListTableView {
            count = trainList.count
        }else if tableView === personTableView {
            count = passengerList.count
        }
        return count
    }
    func tableView(_ tableView: NSTableView, viewFor tableColumn: NSTableColumn?, row: Int) -> NSView? {
        let cell = tableView.makeView(withIdentifier: (tableColumn?.identifier)!, owner: self)
        if tableView === dateTableview {
            if tableColumn?.title == "选择日期"{
                (cell as? NSTableCellView)?.textField?.stringValue = dateArray[row]
            }else {
                for item in (cell?.subviews)!{
                    if item.isKind(of: NSButton.classForCoder()){
                        let btn = item as! NSButton
                        btn.tag = row
                        btn.target = self
                        btn.action = #selector(checkDateAction(_:))
                    }
                }
            }
        }else if tableView === trainListTableView {
            if tableColumn?.title == "选择日期"{
                let dic = trainList[row]
                let txt = "【\(dic["车次"]!)】\(dic["始发站"]!)-\(dic["终点站"]!) \(dic["出发时间"]!)"
                let textFiled = (cell as? NSTableCellView)?.textField
                textFiled?.font = NSFont.systemFont(ofSize: 12)
                textFiled?.stringValue = txt
            }else {
                for item in (cell?.subviews)!{
                    if item.isKind(of: NSButton.classForCoder()){
                        let btn = item as! NSButton
                        btn.tag = row
                        btn.target = self
                        btn.action = #selector(checkTrainAction(_:))
                    }
                }
            }
        }else if tableView === personTableView{
            if tableColumn?.title == "选择日期"{
                let txt = passengerList[row]["passenger_name"] as! String
                let textFiled = (cell as? NSTableCellView)?.textField
                textFiled?.font = NSFont.systemFont(ofSize: 12)
                textFiled?.stringValue = txt
            }else {
                for item in (cell?.subviews)!{
                    if item.isKind(of: NSButton.classForCoder()){
                        let btn = item as! NSButton
                        btn.tag = row
                        btn.target = self
                        btn.action = #selector(checkPassengerAction(_:))
                    }
                }
            }
        }
        
        return cell
    }
    func tableView(_ tableView: NSTableView, shouldSelectRow row: Int) -> Bool {
        return false
    }
    
    func tableView(_ tableView: NSTableView, heightOfRow row: Int) -> CGFloat {
        return 28
    }
    
}

extension ViewController{
    @objc func checkDateAction(_ sender:NSButton){
        let dateStr = dateArray[sender.tag]
        if sender.state == .on {
            selectedDateDic[dateStr] = sender.tag
        }else {
            selectedDateDic.removeValue(forKey: dateStr)
        }
        
        selectedTextv.string = getSelectedStr(selectedDateDic.keys)
    }
    
    func getSelectedStr(_ keys:Dictionary<String, Int>.Keys)->String{
        var str = ""
        for item in keys{
            str += item + ","
        }
        if str.count > 0{
            str.removeLast()
        }
        return str
    }
    
    @objc func checkTrainAction(_ sender:NSButton){
        let dic = trainList[sender.tag]
        let str = dic["车次"] as! String
        if sender.state == .on {
            selectedTrainDic[str] = sender.tag
        }else {
            selectedTrainDic.removeValue(forKey: str)
        }
        
        selectedTrainV.string = getSelectedStr(selectedTrainDic.keys)
    }
    
    @objc func checkPassengerAction(_ sender:NSButton){
        let dic = passengerList[sender.tag]
        let str = dic["passenger_name"] as! String
        if sender.state == .on {
            selectedPassengerDic[str] = sender.tag
        }else {
            selectedPassengerDic.removeValue(forKey: str)
        }
        
        passengerTextV.string = getSelectedStr(selectedPassengerDic.keys)
    }
    
    func uploadInfo(){
        let url = configPath
        guard var dict = getJson(url) as? [String: Any] else{
            return
        }
        fromStationT.stringValue = dict["出发地"] as! String
        toStationT.stringValue = dict["目的地"] as! String
        
        getPassengers()
        getTrainList()
    }
    
    func getPassengers(){
        guard let list = getJson(passengersPath) as? [[String: Any]] else {
            return
        }
        passengerList = list.filter({ (dict) -> Bool in
            if dict["passenger_name"] as! String == "廖乃刚"{
                return true
            }
            return false
        })
        personTableView.reloadData()
    }
    
    func getTrainList(){
        guard let list = getJson(trainListPath) as? [[String: Any]] else {
            return
        }
        trainList = list
        tipL.stringValue = "更新车次列表成功"
        trainListTableView.reloadData()
    }
}
