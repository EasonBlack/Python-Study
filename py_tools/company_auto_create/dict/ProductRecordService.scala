
@ImplementedBy(classOf[ProductRecordServiceImpl])
trait ProductRecordService {
  def searchProductRecord(hqId: Long): Future[Seq[ProductRecord]] 
  def saveProductRecord(m: ProductRecord): Future[Long]
  def updateProductRecord(m: ProductRecord): Future[Unit]
}

@Singleton
class ProductRecordServiceImpl @Inject()(dbConfigProvider: DatabaseConfigProvider) extends BaseDao(dbConfigProvider)
  with ProductRecordService {

  private[this] val _productRecordTables = Tables.ProductRecordTable
 
  override def searcProductRecord(hqId: Long) = { 
    val query = _productRecordTables.filter(t=>t.hqId === hqId)
     runDBAction(query.sortBy(_.id.desc).result)
  }

  override def saveProductRecord(m: ProductRecord) = {
    runDBAction((_productRecordTables returning _productRecordTables.map(_.id)) += m)
  }

  override def updateProductRecord(m: ProductRecord) = {
    runDBAction(_productRecordTables.filter(_.id === m.id).update(m)).map {
      case _ => Unit
    }
  }
}