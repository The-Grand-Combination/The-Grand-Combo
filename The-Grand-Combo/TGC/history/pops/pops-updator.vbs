Option Explicit

Const FileEncoding = 0 ' 0 = ASCII, -1 = Unicode, -2 = System Default
Const FractDigits = 6 ' number of fractional digits

Dim objList, strPath

If WScript.Arguments.Count = 0 then
    CreateObject("WScript.Shell").PopUp "Drop folder(s) and / or file(s) to the script to process", 3, , 48
    WScript.Quit
End If

Set objList = ReadContent(WScript.Arguments)

If objList.Count = 0 Then
    CreateObject("WScript.Shell").PopUp "No files found", 3, , 48
    WScript.Quit
End If

With CreateObject("VBScript.RegExp")
    .Global = True
    .MultiLine = True
    .IgnoreCase = False
    .Pattern = "(\w+=)""([\.\d\(\)\\\*\+/-]*)"""
    For Each strPath In objList
        WriteToFile .Replace(objList(strPath), GetRef("FnReplace")), strPath, FileEncoding
    Next
End With
CreateObject("WScript.Shell").PopUp "Completed", 1, , 64

Function FnReplace(strMatch, strSubMatch1, strSubMatch2, lngPos, strSource)
    Dim strResult
    On Error Resume Next
    strResult = CStr(Round(Eval(strSubMatch2), FractDigits))
    If Err Then
        Err.Clear
        FnReplace = strMatch
    Else
        FnReplace = strSubMatch1 & """" & strResult & """"
    End If
End Function

Function ReadContent(arrList)
    Dim objList, strPath
    Set objList = CreateObject("Scripting.Dictionary")
    For Each strPath In arrList
        AddContent strPath, objList
    Next
    Set ReadContent = objList
End Function

Sub AddContent(strPath, objList)
    Dim objItem
    With CreateObject("Scripting.FileSystemObject")
        If .FileExists(strPath) Then
            objList(strPath) = ReadFromFile(strPath, FileEncoding)
        End If
        If .FolderExists(strPath) Then
            For Each objItem In .GetFolder(strPath).Files
                AddContent objItem.Path, objList
            Next
            For Each objItem In .GetFolder(strPath).SubFolders
                AddContent objItem.Path, objList
            Next
        End If
    End With
End Sub

Function ReadFromFile(strPath, intFormat)
    With CreateObject("Scripting.FileSystemObject").OpenTextFile(strPath, 1, False, intFormat)
        ReadFromFile = ""
        If Not .AtEndOfStream Then ReadFromFile = .ReadAll
        .Close
    End With
End Function

Sub WriteToFile(strCont, strPath, intFormat)
    With CreateObject("Scripting.FileSystemObject").OpenTextFile(strPath, 2, True, intFormat)
        .Write(strCont)
        .Close
    End With
End Sub