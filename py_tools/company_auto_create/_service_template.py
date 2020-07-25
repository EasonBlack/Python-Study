from jinja2 import Template

service_template =  Template('''
@ImplementedBy(classOf[{{entityName}}ServiceImpl])
trait {{entityName}}Service {
  def search{{entityName}}(hqId: Long): Future[Seq[{{entityName}}]] 
  def save{{entityName}}(m: {{entityName}}): Future[Long]
  def update{{entityName}}(m: {{entityName}}): Future[Unit]
}

@Singleton
class {{entityName}}ServiceImpl @Inject()(dbConfigProvider: DatabaseConfigProvider) extends BaseDao(dbConfigProvider)
  with {{entityName}}Service {

  private[this] val _{{tableClassNames}} = Tables.{{tableClassName}}
 
  override def searc{{entityName}}(hqId: Long) = { 
    val query = _{{tableClassNames}}.filter(t=>t.hqId === hqId)
     runDBAction(query.sortBy(_.id.desc).result)
  }

  override def save{{entityName}}(m: {{entityName}}) = {
    runDBAction((_{{tableClassNames}} returning _{{tableClassNames}}.map(_.id)) += m)
  }

  override def update{{entityName}}(m: {{entityName}}) = {
    runDBAction(_{{tableClassNames}}.filter(_.id === m.id).update(m)).map {
      case _ => Unit
    }
  }
}
''')