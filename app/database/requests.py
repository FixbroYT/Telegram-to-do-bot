from sqlalchemy import select

from app.database.models import UserTasks, async_session

async def add_task(task_name, tg_id):
    async with async_session() as session:
        new_task = UserTasks(task=task_name, tg_id=tg_id)
        session.add(new_task)
        await session.commit()

async def task_list(tg_id):
    async with async_session() as session:
        tasks = await session.scalars(select(UserTasks).where(UserTasks.tg_id == tg_id))
        tasks_list = tasks.all()

        if not tasks_list:
            return None


        text = "🧾 Your current tasks:"

        for task in tasks_list:
            text += f"\n- {task.task}"

        return text

async def delete_task(task_name, tg_id):
    async with async_session() as session:
        task = await session.scalar(select(UserTasks).where(UserTasks.task == task_name, UserTasks.tg_id == tg_id))

        if not task:
            return None

        await session.delete(task)
        await session.commit()

        return True

async def clear_tasks(tg_id):
    async with async_session() as session:
        tasks = await session.scalars(select(UserTasks).where(UserTasks.tg_id == tg_id))
        tasks = tasks.all()

        if not tasks:
            return None

        for task in tasks:
            await session.delete(task)

        await session.commit()