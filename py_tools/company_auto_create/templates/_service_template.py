from jinja2 import Template

service_template =  Template('''
@ImplementedBy(classOf[{{entityName}}ServiceImpl])
trait {{entityName}}Service {
  def search{{entityName}}(hqId: Long): Future[Seq[{{entityName}}]] 
  def search{{entityName}}(hqId: Long,  searchPage: SearchPage ): Future[SearchResult[{{entityName}}]] 
  def find{{entityName}}ById(hqId: Long, id: Long) : Future[{{entityName}}]
  def save{{entityName}}(m: {{entityName}}): Future[Long]
  def saveAndUpdate{{entityName}}(m: {{entityName}}): Future[Unit]
  def update{{entityName}}(m: {{entityName}}): Future[Unit]
}

@Singleton
class {{entityName}}ServiceImpl @Inject()(dbConfigProvider: DatabaseConfigProvider) extends BaseDao(dbConfigProvider)
  with {{entityName}}Service {

  private[this] val _{{tableClassNames}} = Tables.{{tableClassNames}}
 
  override def search{{entityName}}(hqId: Long) = { 
    val query = _{{tableClassNames}}.filter(t=>t.hqId === hqId)
    runDBAction(query.sortBy(_.id.desc).result)
  }

  override def search{{entityName}}(hqId: Long, searchPage: SearchPage) = { 
    val query = _{{tableClassNames}}.filter(t=>t.hqId === hqId)
    runDBAction(query.sortBy(_.id.desc).drop((searchPage.page - 1) * searchPage.size).take(searchPage.size).result.zip(
				query.length.result)).map { case (items, count) =>
				DaoHelper.createSearchResult(items, searchPage, count)
		}
  }

  override def find{{entityName}}ById(hqId: Long, id: Long) = {
    val query = _{{tableClassNames}}.filter(t=>t.hqId === hqId && t.id === id)
    runDBAction(query.result.head)
  }
  

  override def save{{entityName}}(m: {{entityName}}) = {
    runDBAction((_{{tableClassNames}} returning _{{tableClassNames}}.map(_.id)) += m)
  }

  override def saveAndUpdate{{entityName}}(m: {{entityName}}) = {
    (m.id match {
      case 0L => runDBAction((_{{tableClassNames}} returning _{{tableClassNames}}.map(_.id)) += m)
      case _ => runDBAction(_{{tableClassNames}}.filter(_.id === m.id).update(m))
    }).map { _
      => Unit
    }
  }

  override def update{{entityName}}(m: {{entityName}}) = {
    runDBAction(_{{tableClassNames}}.filter(_.id === m.id).update(m)).map {
      case _ => Unit
    }
  }
}
''')