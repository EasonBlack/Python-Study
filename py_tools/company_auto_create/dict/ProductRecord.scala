
package entities
import java.sql.Timestamp
case class ProductRecord(
	 id : Long ,  name : String ,  createTime : Timestamp ,  price : Option[Double]  
) extends IdEntity {
}

implicit lazy val  productRecordFormat: Format[ProductRecord] = Json.format[ProductRecord]
class ProductRecordTable(tag: Tag) extends IdTable[ProductRecord](tag, "t_product_record", "f_id") {	def id = column[Long]("f_id")
	def name = column[String]("f_name")
	def createTime = column[Timestamp]("f_create_time")
	def price = column[Option[Double]]("f_price")

	override def * = ( id,  name,  createTime,  price ) <>
	(ProductRecord.tupled, ProductRecord.unapply)
}
lazy val productRecordTables = TableQuery[ProductRecordTable]
