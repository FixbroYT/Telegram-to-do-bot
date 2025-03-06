from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from app.database.requests import add_task, task_list, delete_task, clear_tasks

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("🖐 Hello! Welcome to bot!")

@router.message(Command("add"))
async def cmd_add(message: Message):
    task_test = message.text.split()

    if len(task_test) > 1:
        task_name = message.text.replace("/add", "").strip()
        await add_task(task_name, message.from_user.id)
        await message.answer("✔ Your new task successfully saved!")
    else:
        await message.answer("⚠️ Please specify the task after the /add command.")

@router.message(Command("list"))
async def cmd_list(message: Message):
    answer = await task_list(message.from_user.id)

    if not answer:
        await message.answer("❌ Error. You have no active tasks yet!.")
        return

    await message.answer(answer)

@router.message(Command("delete"))
async def cmd_delete(message: Message):
    task_test = message.text.split()

    if len(task_test) > 1:
        task_name = message.text.replace("/delete", "").strip()
        result = await delete_task(task_name, message.from_user.id)

        if result:
            await message.answer("✔ Your task successfully deleted!")
        else:
            await message.answer("❌ Error. You do not have such a task.")
    else:
        await message.answer("⚠️ Please specify the task after the /delete command.")

@router.message(Command("clear"))
async def cmd_clear(message: Message):
    await clear_tasks(message.from_user.id)
    await message.answer("✔ Your tasks successfully cleared!")