#!/usr/bin/env python3
"""
微信公众号自动化写作与发布技能
"""

import os
import sys
import subprocess

def write_article(topic: str, mode: str = "auto", style: str = None, words: int = 1500):
    """
    自动或引导式写作微信公众号文章
    
    Args:
        topic: 文章主题
        mode: 写作模式，可选值为 'auto' 或 'guided'
        style: 文章风格，仅在引导式模式下有效
        words: 目标字数
    
    Returns:
        文章写作结果（包括标题、内容、大纲等）
    """
    script_path = os.path.join(os.path.dirname(__file__), "scripts", "write_article.py")
    
    if not os.path.exists(script_path):
        return "❌ 技能脚本不存在"
    
    cmd = [sys.executable, script_path, topic, "--mode", mode, "--words", str(words)]
    
    if style and mode == "guided":
        cmd.extend(["--style", style])
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.path.dirname(__file__))
        
        if result.returncode == 0:
            return "✅ 文章写作成功\n" + result.stdout
        else:
            return f"❌ 文章写作失败 (错误码: {result.returncode})\n" + result.stderr
            
    except Exception as e:
        return f"❌ 文章写作过程中发生错误: {str(e)}"

def push_draft(article_file: str, title: str = None, theme: str = None):
    """
    推送文章到微信公众号草稿箱
    
    Args:
        article_file: 文章文件路径（支持 .html 或 .md 文件）
        title: 文章标题（如果文件中没有包含）
        theme: 文章排版主题
    
    Returns:
        推送结果
    """
    script_path = os.path.join(os.path.dirname(__file__), "scripts", "push_draft.py")
    
    if not os.path.exists(script_path):
        return "❌ 技能脚本不存在"
    
    if not os.path.exists(article_file):
        return f"❌ 文章文件不存在: {article_file}"
    
    cmd = [sys.executable, script_path, "--file", article_file]
    
    if title:
        cmd.extend(["--title", title])
    
    if theme:
        cmd.extend(["--theme", theme])
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.path.dirname(__file__))
        
        if result.returncode == 0:
            return "✅ 文章推送成功\n" + result.stdout
        else:
            return f"❌ 文章推送失败 (错误码: {result.returncode})\n" + result.stderr
            
    except Exception as e:
        return f"❌ 文章推送过程中发生错误: {str(e)}"

def list_themes():
    """
    列出所有可用的排版主题
    
    Returns:
        主题列表
    """
    script_path = os.path.join(os.path.dirname(__file__), "scripts", "push_draft.py")
    
    if not os.path.exists(script_path):
        return "❌ 技能脚本不存在"
    
    cmd = [sys.executable, script_path, "--list-themes"]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.path.dirname(__file__))
        
        if result.returncode == 0:
            return "✅ 可用主题:\n" + result.stdout
        else:
            return f"❌ 获取主题列表失败 (错误码: {result.returncode})\n" + result.stderr
            
    except Exception as e:
        return f"❌ 获取主题列表过程中发生错误: {str(e)}"

# 技能入口函数
def main():
    """
    技能入口函数，用于演示技能的主要功能
    """
    print("微信公众号自动化写作与发布技能")
    print("=" * 30)
    print("1. 自动写作: 输入主题即可生成文章")
    print("2. 引导式写作: 可指定风格和字数")
    print("3. 推送草稿: 支持多种主题排版")
    print("4. 主题管理: 查看所有可用主题")
    
    while True:
        print("\n请选择功能:")
        print("1. 自动写作文章")
        print("2. 引导式写作文章")
        print("3. 推送文章到公众号")
        print("4. 列出所有主题")
        print("0. 退出")
        
        choice = input("请输入选项: ")
        
        if choice == "0":
            break
        elif choice == "1":
            topic = input("请输入文章主题: ")
            words = input("请输入目标字数 (默认1500): ")
            words = int(words) if words else 1500
            print(write_article(topic, mode="auto", words=words))
        elif choice == "2":
            topic = input("请输入文章主题: ")
            style = input("请输入文章风格: ")
            words = input("请输入目标字数 (默认1500): ")
            words = int(words) if words else 1500
            print(write_article(topic, mode="guided", style=style, words=words))
        elif choice == "3":
            article_file = input("请输入文章文件路径: ")
            title = input("请输入文章标题 (可选): ")
            theme = input("请输入排版主题 (可选): ")
            print(push_draft(article_file, title=title if title else None, theme=theme if theme else None))
        elif choice == "4":
            print(list_themes())
        else:
            print("❌ 无效选项，请重新输入")

if __name__ == "__main__":
    main()