import click
import Database

db = Database.Database('Task.db')

@click.command()
@click.option('--task', required = True, type = (str, str, str, int))
def new_task(task):
    tup_s = f'{task}'
    db.insert(tup_s, 'TASK')
    click.echo('Your task has been successfully added')